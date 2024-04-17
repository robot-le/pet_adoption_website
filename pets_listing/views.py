from django.shortcuts import render
from django.views import generic
from .models import (
    Pet, Organization,
)


def index(request):
    return render(request, 'index.html')


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
