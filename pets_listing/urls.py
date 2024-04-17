from django.urls import re_path
from . import views


urlpatterns = [
    re_path(r'^$', views.home, name='home'),
    re_path(r'pets/', views.PetListView.as_view(), name='pets'),
    re_path(r'^pet/(?P<pk>\d+)$', views.PetDetailView.as_view(), name='pet_detail'),
    re_path(r'^organizations/', views.OrganizationListView.as_view(), name='organizations'),
    re_path(r'^organization/(?P<pk>\d+)$', views.OrganizationDetailView.as_view(), name='organization_detail'),
    re_path(r'^pet/create/', views.PetCreateView.as_view(), name='pet_create'),
    re_path(r'^organization/create/', views.OrganizationCreateView.as_view(), name='organization_create'),
]
