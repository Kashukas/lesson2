from django.contrib import admin
from . import models

# Register your models here.

class ProfileAdmin(admin.ModelAdmin):
   list_display = [
      'pk',
      'user',
      'phone',
      'country',
      'city',
      'postcode',
      'address1',
      'address2',
      'addit_info',
      ]


admin.site.register(models.Profile, ProfileAdmin)