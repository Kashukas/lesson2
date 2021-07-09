from django.contrib import messages
from django.contrib.messages.api import get_messages
from django.db.models.fields import EmailField
from django.shortcuts import render

# Create your views here.

from django.urls import reverse_lazy, reverse
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.contrib.auth import forms, get_user_model, login
from django.views.generic import FormView, DetailView, ListView, DeleteView
from django.views.generic.edit import UpdateView
from . import forms as users_forms
from . import models
from django.db import IntegrityError
from django.http import HttpResponseRedirect


User = get_user_model()
 
class PwdChangeView(PasswordChangeView):
    form_class = forms.PasswordChangeForm
    template_name="users/pch.html"

class UserLoginView(LoginView):
    template_name="users/login.html"
    success_url = reverse_lazy('login')

class UserLogoutView(LogoutView):
    template_name="users/logout.html"
    next_page = "/"

class RegisterView(FormView):
    template_name = "users/create-user.html"
    form_class = users_forms.RegisterForm
    success_url = reverse_lazy('main-page')
    def form_valid(self, form):
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password2')
        first_name = form.cleaned_data.get('first_name')
        last_name = form.cleaned_data.get('last_name')
        email = form.cleaned_data.get('email')
        phone = form.cleaned_data.get('phone')
        country = form.cleaned_data.get('country')
        city = form.cleaned_data.get('city')
        postcode = form.cleaned_data.get('postcode')
        address1 = form.cleaned_data.get('address1')
        address2 = form.cleaned_data.get('address2')
        addit_info = form.cleaned_data.get('addit_info')
        try:
            user = User.objects.create_user(
                username=username, 
                password=password, 
                first_name=first_name, 
                last_name=last_name,
                email=email,
                )
            profile = models.Profile.objects.create(
                user=user,
                phone=phone,
                country=country,
                city=city,
                postcode=postcode,
                address1=address1,
                address2=address2,
                addit_info=addit_info
                )
            login(self.request, user)
            return super().form_valid(form)
        except IntegrityError:
            messages.add_message(
            self.request, messages.INFO, 
            f'Пользователь с именем {str(username)} уже существует! Введите другое имя пользователя.'
            )
            return HttpResponseRedirect(reverse_lazy('user:register'))

# class UserUpdateView(UpdateView):
#     model = User
#     form_class = users_forms.RegisterForm
#     template_name = "users/update-user.html"


class UserUpdateView(FormView):
    template_name = "users/update-user.html"
    form_class = users_forms.RegisterForm
    success_url = reverse_lazy('main-page')
    def get_initial(self):
        pk = self.request.user.pk
        username = self.request.user.username
        password = self.request.user.password
        first_name = self.request.user.first_name
        last_name = self.request.user.last_name
        email = self.request.user.email
        phone = self.request.user.profile.phone
        country = self.request.user.profile.country
        city = self.request.user.profile.city
        postcode = self.request.user.profile.postcode
        address1 = self.request.user.profile.address1
        address2 = self.request.user.profile.address2
        addit_info = self.request.user.profile.addit_info
        return {'username': username,
        'password': password,
        'first_name': first_name,
        'last_name': last_name,
        'email': email,
        'phone': phone,
        'country': country,
        'city': city,
        'postcode': postcode,
        'address1': address1,
        'address2': address2,
        'addit_info': addit_info,
        }

    def form_valid(self, form):
        pk = self.request.user.pk
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password2')
        first_name = form.cleaned_data.get('first_name')
        last_name = form.cleaned_data.get('last_name')
        email = form.cleaned_data.get('email')
        phone = form.cleaned_data.get('phone')
        country = form.cleaned_data.get('country')
        city = form.cleaned_data.get('city')
        postcode = form.cleaned_data.get('postcode')
        address1 = form.cleaned_data.get('address1')
        address2 = form.cleaned_data.get('address2')
        addit_info = form.cleaned_data.get('addit_info')
        user = User.objects.filter(pk=pk).update(
            username=username, 
            password=password, 
            first_name=first_name, 
            last_name=last_name,
            email=email,
            )
        print(models.Profile.objects.filter(user=User.objects.get(pk=pk)))
        profile = models.Profile.objects.filter(user=User.objects.get(pk=pk)).update(
            user=user,
            phone=phone,
            country=country,
            city=city,
            postcode=postcode,
            address1=address1,
            address2=address2,
            addit_info=addit_info
            )
        login(self.request, user)
        return super().form_valid(form)
    pass

class UserDetailView(DetailView):
    model = models.User
    template_name = 'users/user-detail.html'

class UserListView(ListView):
    model = models.User
    template_name = 'users/user-list.html'

class UserDeleteView(DeleteView):
    model = models.User
    success_url = reverse_lazy('user:users')
    template_name = 'users/user_confirm_delete.html'