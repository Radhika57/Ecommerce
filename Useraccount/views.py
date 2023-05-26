
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth import  logout
from django.views import generic
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView
from django.shortcuts import render,redirect
from django.views import generic
from django.views.generic import TemplateView
from django.views.generic import ListView
from django.shortcuts import (get_object_or_404,
                              render,
                              HttpResponseRedirect)

from Useraccount.models import User
from Useraccount.forms import *

class LoginView(LoginView):
    form_class = LoginForm
    template_name = 'account/login.html'
    def get_success_url(self):
        if self.request.user.is_authenticated:
            return reverse_lazy('dashboard')
        else:
            return super().get_success_url()

class RegisterView(generic.CreateView):
    form_class = RegisterForm
    template_name = 'account/signup.html'
    success_url = reverse_lazy('login')


def logoutPage(Request):
    logout(Request)
    return redirect("/admin")
