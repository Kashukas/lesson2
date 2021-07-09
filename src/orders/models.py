from django.contrib.contenttypes.fields import GenericRelation
from django.db import models
from carts.models import Cart
from comments.models import Comment
from manuals.models import Status
from django.contrib.contenttypes.fields import GenericRelation
from comments.models import Comment

# Create your models here.

# это д.б. в отдельном приложении для заказов
class Order(models.Model):
    cart = models.ForeignKey(
        Cart,
        on_delete=models.PROTECT,
        verbose_name='Заказ'
    )
    status = models.ForeignKey(
        Status,
        on_delete=models.PROTECT,
        verbose_name="Статус заказа",
        default=1
    )
    contact_info = models.TextField(verbose_name="Контактная информация")
    created = models.DateTimeField(
        verbose_name="Дата внесения в каталог",
        auto_now=False, 
        auto_now_add=True
    )
    updated = models.DateTimeField(
        verbose_name="Дата последнего изменения",
        auto_now=True, 
        auto_now_add=False
    )
    comment = GenericRelation(Comment)