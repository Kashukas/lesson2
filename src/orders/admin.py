from django.contrib import admin
from . import models

# Register your models here.

class OrderAdmin(admin.ModelAdmin):
   list_display = ['pk', 'contact_info', 'created', 'updated', 'status']

admin.site.register(models.Order, OrderAdmin)