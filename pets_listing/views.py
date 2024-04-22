from django.contrib.auth import get_user_model
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Permission
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    PermissionRequiredMixin,
    UserPassesTestMixin,
)
from django.shortcuts import (
    render,
    redirect,
    get_object_or_404,
)
from django.urls import reverse_lazy
from django.views import generic
from .models import (
    Pet,
    Media,
    Organization,
)
from .forms import (
    UploadMediaForm,
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


@login_required(login_url='login')
def pet_create(request):
    if request.method == 'POST':
        pet_form = CreatePetProfileForm(request.POST)
        media_form = UploadMediaForm(request.POST, request.FILES)
        if pet_form.is_valid() and media_form.is_valid():
            pet_obj = pet_form.save(commit=False)
            pet_obj.profile_creator = request.user
            try:
                pet_obj.organization = request.user.org
            except get_user_model().org.RelatedObjectDoesNotExist:
                pass
            pet_obj.save()

            files = media_form.cleaned_data['file']
            for file in files:
                file_obj = Media(file=file, pet=pet_obj)
                file_obj.save()

            return redirect('pet_detail', pk=pet_obj.pk)
    else:
        pet_form = CreatePetProfileForm()
        media_form = UploadMediaForm()
    return render(
        request,
        'pets_listing/pet_form.html',
        {
            'title': 'Create a Pet profile',
            'pet_form': pet_form,
            'media_form': media_form,
        },
    )


@login_required(login_url='login')
def pet_update(request, pk):

    print()

    if not bool(request.user.pets.filter(pk=int(pk))):
        raise PermissionDenied

    pet = get_object_or_404(Pet, pk=pk)
    pet_form = CreatePetProfileForm(instance=pet)
    media_form = UploadMediaForm(instance=pet)

    if request.method == 'POST':
        pet_form = CreatePetProfileForm(request.POST, instance=pet)
        media_form = UploadMediaForm(request.POST, request.FILES, instance=pet)

        if pet_form.is_valid() and media_form.is_valid():
            pet_obj = pet_form.save()

            files = media_form.cleaned_data['file']
            for file in files:
                file_obj = Media(file=file, pet=pet_obj)
                file_obj.save()

            return redirect('pet_detail', pk=pet_obj.pk)
    return render(
        request,
        'pets_listing/pet_form.html',
        {
            'title': 'Create a Pet profile',
            'pet_form': pet_form,
            'media_form': media_form,
        },
    )


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
