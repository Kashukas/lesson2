from django.shortcuts import render
from . import models, forms
from django.views.generic import FormView, DetailView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect, request
from django.views import View
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from . import forms
from django.db.models import Q


# Create your views here.

class CreateOrderView(LoginRequiredMixin, FormView):
    #messages.add_message(self.request, messages.INFO, 'Спасибо! Для продолжения оформения вашего заказа зарегистрируйтесь или авторизуйтесь.')
    form_class = forms.OrderCreateForm
    template_name = 'orders/order-create.html'
    login_url = 'user:login'
    redirect_field_name = 'redirect_to'

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
        phone = form.cleaned_data.get('phone')
        order = models.Order.objects.create(
            cart=cart,
            contact_info = ci,
            phone=phone
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

class OrderListView(PermissionRequiredMixin, ListView):
    model = models.Order
    permission_required = 'books.add_book'
    paginate_by = 10
    template_name = 'orders/order-list.html'
    # Filter orders list:
    def get_queryset(self):
        qs = super().get_queryset()
        filter = self.request.GET.get('filter')
        search_data = self.request.GET.get('q') # Данные введенные в окне 'Поиск'
        if filter == 'new':
            return qs.filter(status=1)
        if filter == 'paid':
            return qs.filter(status=2)
        if filter == 'in_pr':
            return qs.filter(status=3)
        if filter == 'prd':
            return qs.filter(status=4)
        if filter == 'dlvrd':
            return qs.filter(status=5)
        try:
            if filter[0:4] == 'user':
                return qs.filter(Q(cart__customer__username__icontains=filter[5:]))
        except TypeError:
            pass        
        if search_data:
            return qs.filter(Q(cart__customer__username__icontains=search_data) | Q(status__order_status__icontains=search_data)) # Условие или - |
        return qs

class OrderDetailView(DetailView):
    model = models.Order
    template_name = 'orders/order-detail.html'

class OrderUpdateView(UpdateView):
    model = models.Order
    form_class = forms.OrderUpdateForm
    template_name = "orders/order-create.html"

class OrderDeleteView(DeleteView):
    model = models.Order
    template_name = "orders/order_confirm_delete.html"
    success_url = reverse_lazy('order:orders')