from django import forms

class OrderCreateForm(forms.Form):
    contact_info = forms.CharField(label="Контактная информация", required=True, widget=forms.TextInput)
    tel = forms.CharField(label="Телефон", required=True, widget=forms.TextInput)