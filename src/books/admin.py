from django.contrib import admin

# Register your models here.
from . import models

class BookAdmin(admin.ModelAdmin):
   list_display = ['pk',
    'name',
    'pic',
    'price',
    'serie',
    'genre',
    'year',
    'pages',
    'binding',
    'format',
    'isbn',
    'weight',
    'age_rating',
    'publisher',
    'avail_quan',
    'active',
    'rating',
    'created',
    'updated',
    'description']

admin.site.register(models.Book, BookAdmin)
