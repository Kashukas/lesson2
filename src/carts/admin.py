from django.contrib import admin
from . import models

# Register your models here.

class CartAdmin(admin.ModelAdmin):
   list_display = ['pk', ]

class BookInCartAdmin(admin.ModelAdmin):
   list_display = ['pk', 'cart', 'book', 'quantity', 'unit_price']

class OrderAdmin(admin.ModelAdmin):
   list_display = ['pk', 'contact_info', 'created', 'updated']

admin.site.register(models.Cart, CartAdmin)
admin.site.register(models.BookInCart, BookInCartAdmin)
admin.site.register(models.Order, OrderAdmin)