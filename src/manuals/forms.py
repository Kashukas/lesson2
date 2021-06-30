from django import forms
from django.db.models import fields

from . import models

# такая форма исп-ся, где не используется БД
#class CreateAuthorForm(forms.Form):   
    #name = forms.CharField(
    #    required=True,
    #    label="Имя автора"
    #)
    #description = forms.CharField(
    #    required=True,
    #    label="Краткое описание"
    #)

class CreateAuthorForm(forms.ModelForm):
    #description = forms.CharField(forms.)
    class Meta:
        model = models.Author
        fields = (
            'name',
            'description',
        )
            # или '__all__' если все поля надо

    # Проверка значений в полях:    
    #def clean_name(self):
    #    value = self.cleaned_data.get('name')
    #    if value > 1:
    #        raise ValidationError("Неверное имя")
    #    return value

class CreateSerieForm(forms.ModelForm):
    class Meta:
        model = models.Serie
        fields = (
            'bookserie',
            'books_quantity',
        )

class CreateGenreForm(forms.ModelForm):
    class Meta:
        model = models.Genre
        fields = (
            'genre_name',
            'description',
        )

class CreatePublisherForm(forms.ModelForm):
    class Meta:
        model = models.Publisher
        fields = (
            'publisher_name',
        )    

class CreateStatusForm(forms.ModelForm):
    class Meta:
        model = models.Status
        fields = (
            'order_status',
        )    