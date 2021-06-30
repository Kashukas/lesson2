from django.db import models
from carts.models import Cart

# Create your models here.

# это д.б. в отдельном приложении для заказов
class Order(models.Model):
    cart = ForeignKey(
        Cart,
        on_delete=models.PROTECT,
        verbose_name='Заказ'
    )
    #status = models.ForeignKey(OrderStatus)
    contact_info = models.TextField(verbose_name="Контактная инфорамация")
    created = models.DateTimeField(
        verbose_name="Дата внесения в каталог",
        auto_now=False, 
        auto_now_add=True)
    updated = models.DateTimeField(
        verbose_name="Дата последнего изменения",
        auto_now=True, 
        auto_now_add=False)