from abc import ABC
import django
from django.db.models.fields import DecimalField
from django.views.generic import UpdateView, DetailView, FormView
from django.views import View
from django.http import HttpResponseRedirect
from django.views.generic.edit import DeleteView
from . import models

from books import models as books_models
from django.urls import reverse_lazy
# Create your views here.


class CartView(DetailView):
    template_name = 'carts/cart-edit.html'
    model = models.Cart

    def get_object(self, queryset=None):
        # get cart
        cart_id = self.request.session.get('cart_id')
        cart, created = models.Cart.objects.get_or_create(
            pk = cart_id,
            defaults={},
        )
        if created:
            self.request.session['cart_id'] = cart.pk
        # get book_in_cart
        book_id = self.request.GET.get('book_id') # Достаем из запроса атрибут book_id
        if book_id:
            book = books_models.Book.objects.get(pk=int(book_id))
            book_in_cart, book_created = models.BookInCart.objects.get_or_create(
                cart=cart,
                book=book,
                defaults={
                    'unit_price': book.price
                }
            )
            if not book_created:
                # Позиция продукта в корзине
                q = book_in_cart.quantity + 1
                book_in_cart.quantity = q
                book_in_cart.save()
        return cart

class DeleteGoodInCartView(DeleteView):
    model = models.BookInCart
    success_url = reverse_lazy('cart:cart-edit')


class CartUpdate(View):
    def post(self, request):
        action = request.POST.get('submit')
        cart_id = self.request.session.get('cart_id')
        cart, created = models.Cart.objects.get_or_create(
            pk = cart_id,
            defaults={},
        )
        if created:
            self.request.session['cart_id'] = cart.pk
        goods = cart.goods.all()
        if goods:
            for key, value in request.POST.items():
                if 'quantityforgood_' in key:
                    pk = int(key.split('_')[1])
                    good = goods.get(pk=pk)
                    good.quantity = int(value)
                    good.save()
        if action == 'save_cart':
            return HttpResponseRedirect(reverse_lazy('cart:cart-edit'))
        elif action == 'create_order':
            return HttpResponseRedirect(reverse_lazy('cart:create-order'))
        else:
            return HttpResponseRedirect(reverse_lazy('cart:cart-edit'))

