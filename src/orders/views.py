from django.shortcuts import render
from . import models, forms
from django.views.generic import FormView
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
import django


# Create your views here.

class CreateOrderView(FormView):
    form_class = forms.OrderCreateForm
    template_name = 'carts/create-order.html'
    #success_url = reverse_lazy('#страница с благодарностью за заказ')

    def get_initial(self):
        if self.request.user.is_anonymous:
            return {}
        tel = self.request.user.profile.tel # profile - отдельная таблица, tel - поле в таблице
        return {'contact_info': "Contact!!", 'tel': tel}

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
        self.request.session.delete('cart_id') #проверить очищает ли из сессии cart_id
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        card_id = self.request.session.get('cart_id')
        cart, created = models.Cart.objects.get_or_create(
            pk=cart_id,
            defaults={}
        )
        context['object'] = cart
        return context