from django.shortcuts import render

# Create your views here.

from django.urls import reverse_lazy, reverse
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.contrib.auth import forms

    
class PwdChangeView(PasswordChangeView):
    form_class = forms.PasswordChangeForm
    template_name="users/pch.html"

class UserLoginView(LoginView):
    template_name="users/login.html"
    success_url = reverse_lazy('login')

