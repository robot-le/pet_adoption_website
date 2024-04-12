from django.urls import path, re_path
from . import views


urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    re_path(r'pets/', views.PetListView.as_view(), name='pets'),
    re_path(r'^pet/(?P<pk>\d+)$', views.PetDetailView.as_view(), name='pet-detail'),
]
