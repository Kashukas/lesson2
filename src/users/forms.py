from django import forms
from django.contrib.auth import password_validation, get_user_model
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.contrib.auth.password_validation import validate_password
from django.core import validators
from django.core.exceptions import ValidationError
from django.db import models


User = get_user_model()

username_validator = UnicodeUsernameValidator()

# Про валидацию телефонного номера см. в лекции от 28.06.2021 на 1:12:30
def phone_validator(value): # Валидация телефонного номера.
    try:
        for i in range(0,9):
            int(value[i])
    except ValueError:
        raise ValidationError(
                "Неверно введен номер. Введите 9 цифр номера телефона в формате: 25ххххххх, 29ххххххх, 33ххххххх, 44ххххххх",
                params={'value': value},
                )

#def is_username_unique(username):
    # сделать проверку на уникальность пользователя
    # добавить is_user_unique в валидаторы username

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=150, required=True, label="Имя пользователя", validators=[username_validator])
    password1 = forms.CharField(
        label="Пароль",
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label="Подтверждение пароля",
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        strip=False,
        help_text="Для проверки введите тот же пароль, что и раньше.",
    )
    first_name = forms.CharField(label='Имя', max_length=150, required=False)
    last_name = forms.CharField(label='Фамилия', max_length=150, required=False)
    email = forms.EmailField(label='email', required=False)
    phone = forms.CharField(
        label='Номер телефона', 
        max_length="9", 
        required=True, 
        help_text="Введите 9 цифр номера телефона в формате: 25ххххххх, 29ххххххх, 33ххххххх, 44ххххххх",
        validators=[phone_validator])
    country = forms.CharField(label="Страна", max_length=200, required=False)
    city  = forms.CharField(label='Город', max_length=200, required=False)
    postcode  = forms.IntegerField(label='Почтовый индекс', required=False)
    address1  = forms.CharField(label='Адрес 1', required=False)
    address2  = forms.CharField(label='Адрес 2', required=False)
    addit_info  = forms.CharField(label='Дополнительная информация', required=False)

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError(
                'Введенные пароли не совпадают',
                code='password_mismatch',
            )
        try:
            validate_password(password2, User)
        except ValidationError as error:
            self.add_error('password2', error)
        return password2