from django.contrib import admin
from .models import *

admin.site.register(Breed)
admin.site.register(City)


class PetInline(admin.TabularInline):
    model = Pet
    extra = 0


@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner', 'city')
    inlines = [PetInline]


class PetAdmin(admin.ModelAdmin):
    list_display = ('name', 'profile_creator', 'organization', 'city')
