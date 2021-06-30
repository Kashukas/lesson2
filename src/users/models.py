from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.

from django.urls import reverse

from manuals.models import Author, Serie, Genre, Publisher
#from django.utils.translation import gettext_lazy as _


from django.contrib.auth.models import User, Group
from django.contrib.auth import get_user_model
# Create your models here.

class UserAddress(models.Model):
    country = models.CharField(verbose_name="Страна", max_length=200)
    city = models.CharField(verbose_name="Город", max_length=200)
    postcode = models.IntegerField(verbose_name="Почтовый индекс")
    address1 = models.TextField(verbose_name="Адрес 1")
    address2 = models.TextField(verbose_name="Адрес 2", default='---')

    def __str__(self) -> str:
        return self.address1 + ', ' + self.city + ', ' + self.country

    def get_absolute_url(self):
        return reverse('address:addresses') #args=[self.pk]

    class Meta:
        verbose_name = "Адрес"
        verbose_name_plural = "Адреса"

class UserGroup(Group):
    pass

class Customer(User):
    #login = models.CharField(verbose_name="Логин", max_length=200)
    #password = models.CharField(verbose_name="Пароль", max_length=200)
    #mail =models.EmailField(verbose_name="E-mail")
    #firstname = models.CharField(verbose_name="Имя", max_length=300)
    #surname = models.CharField(verbose_name="Фамилия", max_length=300)
    phone = models.CharField(verbose_name="Телефон", max_length=300)
    #group = 
    address = models.OneToOneField(
        UserAddress, 
        on_delete=models.PROTECT,
        related_name='customer_address',
        verbose_name="Домашний адрес"
        )
    addit_info = models.TextField(verbose_name="Адрес 2", default='---')
    
    def __str__(self) -> str:
        return self.phone

    def get_absolute_url(self):
        return reverse('user:users') #args=[self.pk]

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

User = get_user_model()

class Profile(models.Model):
    user = models.OneToOneField(
        User,
        verbose_name="Аккаунт пользователя",
        on_delete=models.CASCADE,
        related_name="profile"
    )
    phone = models.CharField(
        verbose_name="Телефон",
        max_length=15
    )