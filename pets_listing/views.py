from django.shortcuts import render
from django.views import generic
from .models import (
    Pet,
)


def index(request):
    return render(request, 'index.html')


class PetListView(generic.ListView):
    model = Pet
    paginate_by = 2


class PetDetailView(generic.DetailView):
    model = Pet
