from django.contrib import admin
from . import models

# Register your models here.

class CartAdmin(admin.ModelAdmin):
   list_display = ['pk', 'customer', 'created', 'updated']
class BookInCartAdmin(admin.ModelAdmin):
   list_display = ['pk', 'cart', 'book', 'quantity', 'unit_price']


admin.site.register(models.Cart, CartAdmin)
admin.site.register(models.BookInCart, BookInCartAdmin)