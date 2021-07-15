from django import forms
from . import models


class OrderCreateForm(forms.Form):
    contact_info = forms.CharField(label="Контактная информация", required=True, widget=forms.TextInput)
    phone = forms.CharField(label="Телефон", required=True, widget=forms.TextInput)


class OrderUpdateForm(forms.ModelForm):
        class Meta:
            model = models.Order
            fields = (
                'status',
                'contact_info',
                'phone',
            )