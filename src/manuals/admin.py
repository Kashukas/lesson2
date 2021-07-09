from django.contrib import admin

# Register your models here.
from . import models

class AuthorAdmin(admin.ModelAdmin):
   list_display = ['name', 'description']

class SerieAdmin(admin.ModelAdmin):
    list_display = ['bookserie', 'books_quantity']

class GenreAdmin(admin.ModelAdmin):
    list_display = ['genre_name', 'description']

class StatusAdmin(admin.ModelAdmin):
    list_display = ['pk','order_status']

admin.site.register(models.Author, AuthorAdmin)
admin.site.register(models.Serie, SerieAdmin)
admin.site.register(models.Publisher)
admin.site.register(models.Genre, GenreAdmin)
admin.site.register(models.Status, StatusAdmin)
