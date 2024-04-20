from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.models import Permission

from .forms import (
    LoginUserForm,
    RegisterUserForm,
)


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'users/login.html'
    extra_context = {'title': 'Авторизация'}


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'users/register.html'
    extra_context = {'title': "Регистрация"}
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        obj = form.save()
        obj.user_permissions.add(Permission.objects.get(codename='add_organization'))
        obj.user_permissions.add(Permission.objects.get(codename='change_organization'))
        obj.user_permissions.add(Permission.objects.get(codename='delete_organization'))
        return super().form_valid(form)
