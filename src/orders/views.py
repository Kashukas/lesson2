from django.shortcuts import render
from . import models, forms
from django.views.generic import FormView, DetailView
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect, request
from django.views import View
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.

class CreateOrderView(LoginRequiredMixin, FormView):
    #messages.add_message(self.request, messages.INFO, 'Спасибо! Для продолжения оформения вашего заказа зарегистрируйтесь или авторизуйтесь.')
    form_class = forms.OrderCreateForm
    template_name = 'orders/create-order.html'
    login_url = 'user:login'
    #redirect_field_name = 'user:register'

    def get_initial(self):
        if self.request.user.is_anonymous:
            return {}
        address = self.request.user.profile.address1
        country = self.request.user.profile.country
        city = self.request.user.profile.city
        phone = self.request.user.profile.phone
        return {'contact_info': country + ', ' + city + ', ' + address, 'phone': phone}

    def form_valid(self, form):
        cart_id = self.request.session.get('cart_id')
        cart, created = models.Cart.objects.get_or_create(
            pk = cart_id,
            defaults={},
        )
        if created:
            return HttpResponseRedirect(reverse_lazy('cart:cart-edit'))
        ci = form.cleaned_data.get('contact_info')
        order = models.Order.objects.create(
            cart=cart,
            contact_info = ci
        )
        del self.request.session['cart_id']
        messages.add_message(
            self.request, messages.INFO, 
            f'Спасибо, {str(self.request.user)}! Ваш заказ cоздан. Номер вашего заказа - { order.pk }. Ожидайте, пока с вами свяжется менеджер.'
            )
        return HttpResponseRedirect(reverse_lazy('cart:cart-edit'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart_id = self.request.session.get('cart_id')
        cart, created = models.Cart.objects.get_or_create(
            pk=cart_id,
            defaults={}
        )
        context['object'] = cart
        return context