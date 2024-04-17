from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from .models import (
    Pet, Organization,
)


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


class PetCreateView(generic.CreateView):
    model = Pet
    fields = '__all__'
    extra_context = {
        'title': 'Create a Pet profile',
    }


class PetUpdateView(generic.UpdateView):
    model = Pet
    fields = '__all__'
    extra_context = {
        'title': 'Update a Pet profile',
    }


class PetDeleteView(generic.DeleteView):
    model = Pet
    success_url = reverse_lazy('pets')


class OrganizationCreateView(generic.CreateView):
    model = Organization
    fields = '__all__'
    extra_context = {
        'title': 'Create an Organization',
    }


class OrganizationUpdateView(generic.UpdateView):
    model = Organization
    fields = '__all__'
    extra_context = {
        'title': 'Update an Organization',
    }


class OrganizationDeleteView(generic.DeleteView):
    model = Organization
    success_url = reverse_lazy('organizations')
