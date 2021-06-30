from django import forms
from django.db.models import fields

from . import models


class CreateBookForm(forms.ModelForm):
    class Meta:
        model = models.Book
        fields = (
            'name',
            'pic',
            'price',
            'author',
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
            'description',
        )