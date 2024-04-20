from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    PermissionRequiredMixin,
    UserPassesTestMixin,
)
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from .models import (
    Pet,
    Organization,
)
from .forms import (
    CreatePetProfileForm,
    CreateOrganizationForm,
)


def home(request):
    return render(request, 'home.html')


class PetListView(generic.ListView):
    model = Pet
    paginate_by = 5


class PetDetailView(generic.DetailView):
    model = Pet


class OrganizationListView(generic.ListView):
    model = Organization
    paginate_by = 5


class OrganizationDetailView(generic.DetailView):
    model = Organization


class PetCreateView(LoginRequiredMixin, generic.CreateView):
    form_class = CreatePetProfileForm
    template_name = 'pets_listing/pet_form.html'
    extra_context = {
        'title': 'Create a Pet profile',
    }

    def form_valid(self, form):
        w = form.save(commit=False)
        w.profile_creator = self.request.user
        try:
            w.organization = self.request.user.org
        except get_user_model().org.RelatedObjectDoesNotExist:
            pass
        return super().form_valid(form)


class PetUpdateView(
    LoginRequiredMixin,
    UserPassesTestMixin,
    generic.UpdateView,
):
    model = Pet
    form_class = CreatePetProfileForm
    template_name = 'pets_listing/pet_form.html'
    extra_context = {
        'title': 'Update a Pet profile',
    }

    def test_func(self):
        return bool(self.request.user.pets.filter(pk=int(self.kwargs.get('pk'))))


class PetDeleteView(
    LoginRequiredMixin,
    UserPassesTestMixin,
    generic.DeleteView,
):
    model = Pet
    success_url = reverse_lazy('pets')

    def test_func(self):
        return bool(self.request.user.pets.filter(pk=int(self.kwargs.get('pk'))))


class OrganizationCreateView(
    PermissionRequiredMixin,
    LoginRequiredMixin,
    generic.CreateView,
):
    form_class = CreateOrganizationForm
    template_name = 'pets_listing/organization_form.html'
    permission_required = 'pets_listing.add_organization'
    extra_context = {
        'title': 'Create an Organization',
    }

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.owner = self.request.user
        self.request.user.user_permissions.remove(
            Permission.objects.get(codename='add_organization'),
        )
        return_value = super().form_valid(form)

        for pet in self.request.user.pets.all():
            pet.organization = self.request.user.org
            pet.save()

        return return_value


class OrganizationUpdateView(
    PermissionRequiredMixin,
    LoginRequiredMixin,
    UserPassesTestMixin,
    generic.UpdateView,
):
    model = Organization
    form_class = CreateOrganizationForm
    template_name = 'pets_listing/organization_form.html'
    permission_required = 'pets_listing.change_organization'
    extra_context = {
        'title': 'Update an Organization',
    }

    def test_func(self):
        try:
            return str(self.request.user.org.pk) == str(self.kwargs.get('pk'))
        except get_user_model().org.RelatedObjectDoesNotExist:
            return False


class OrganizationDeleteView(
    PermissionRequiredMixin,
    LoginRequiredMixin,
    UserPassesTestMixin,
    generic.DeleteView,
):
    model = Organization
    permission_required = 'pets_listing.delete_organization'
    success_url = reverse_lazy('organizations')

    def test_func(self):
        try:
            return str(self.request.user.org.pk) == str(self.kwargs.get('pk'))
        except get_user_model().org.RelatedObjectDoesNotExist:
            return False

    def form_valid(self, form):
        self.request.user.user_permissions.add(
            Permission.objects.get(codename='add_organization'),
        )
        return super().form_valid(form)
