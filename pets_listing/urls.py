from django.urls import re_path
from . import views


urlpatterns = [
    re_path(r'^$', views.home, name='home'),
    re_path(r'pets/', views.PetListView.as_view(), name='pets'),
    re_path(r'^pet/(?P<pk>\d+)$', views.PetDetailView.as_view(), name='pet_detail'),
    re_path(r'^organizations/', views.OrganizationListView.as_view(), name='organizations'),
    re_path(r'^organization/(?P<pk>\d+)$', views.OrganizationDetailView.as_view(), name='organization_detail'),
    re_path(r'^pet/add/', views.PetCreateView.as_view(), name='pet_create'),
    re_path(r'^pet/(?P<pk>\d+)/edit/', views.PetUpdateView.as_view(), name='pet_update'),
    re_path(r'pet/(?P<pk>\d+)/delete/', views.PetDeleteView.as_view(), name='pet_delete'),
    re_path(r'^organization/add/', views.OrganizationCreateView.as_view(), name='organization_create'),
    re_path(r'^organization/(?P<pk>\d+)/edit/', views.OrganizationUpdateView.as_view(), name='organization_update'),
    # re_path(r'organization/(?P<pk>\d+)/delete/', views.OrganizationDeleteView.as_view(), name='organization_delete'),
]
