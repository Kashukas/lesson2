from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import Group, Permission
#from django.utils.translation import gettext_lazy as _


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
    country = models.CharField(verbose_name="Страна", max_length=200, default='---')
    city = models.CharField(verbose_name="Город", max_length=200)
    postcode = models.IntegerField(verbose_name="Почтовый индекс")
    address1 = models.TextField(verbose_name="Адрес 1")
    address2 = models.TextField(verbose_name="Адрес 2", default='---')
    addit_info = models.TextField(verbose_name="Дополнительная информация", default='---')

