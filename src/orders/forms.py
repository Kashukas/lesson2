from django import forms


class OrderCreateForm(forms.Form):
    contact_info = forms.CharField(label="Контактная информация", required=True, widget=forms.TextInput)
    phone = forms.CharField(label="Телефон", required=True, widget=forms.TextInput)