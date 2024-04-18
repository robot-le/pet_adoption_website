from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from .models import (
    Pet,
    Organization,
)
from .forms import CreatePetProfileForm, CreateOrganizationForm


def home(request):
    return render(request, 'home.html')


class PetListView(generic.ListView):
    model = Pet
    paginate_by = 2


class PetDetailView(generic.DetailView):
    model = Pet


class OrganizationListView(generic.ListView):
    model = Organization
    paginate_by = 2


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
        w.organization = self.request.user.org
        return super().form_valid(form)


class PetUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Pet
    form_class = CreatePetProfileForm
    template_name = 'pets_listing/pet_form.html'
    extra_context = {
        'title': 'Update a Pet profile',
    }


class PetDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Pet
    success_url = reverse_lazy('pets')


class OrganizationCreateView(LoginRequiredMixin, generic.CreateView):
    form_class = CreateOrganizationForm
    template_name = 'pets_listing/organization_form.html'
    extra_context = {
        'title': 'Create an Organization',
    }

    def form_valid(self, form):
        w = form.save(commit=False)
        w.owner = self.request.user
        return super().form_valid(form)


class OrganizationUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Organization
    form_class = CreateOrganizationForm
    template_name = 'pets_listing/organization_form.html'
    extra_context = {
        'title': 'Update an Organization',
    }


class OrganizationDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Organization
    success_url = reverse_lazy('organizations')
