from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.fields.related import ForeignKey

from books import models as books_models
# Create your models here.

User = get_user_model()

class Cart(models.Model):
    customer = models.ForeignKey(
        User,
        null=True,
        blank=True,
        related_name="carts",
        verbose_name="Корзина",
        on_delete=models.PROTECT
    )
    created = models.DateTimeField(
        verbose_name="Дата создания",
        auto_now=False, 
        auto_now_add=True)
    updated = models.DateTimeField(
        verbose_name="Дата последнего изменения",
        auto_now=True, 
        auto_now_add=False)

    @property # Декоратор для удобства, чтобы м.б. обращаться как к свойству
    def total_price(self):
        total_price = 0
        goods = self.goods.all()
        for good in goods:
            total_price += good.total_price
        return total_price


    #def __str__(self):
    #    return super().__str__()

class BookInCart(models.Model):
    cart = models.ForeignKey(
        Cart,
        on_delete=models.CASCADE,
        verbose_name='Корзина',
        related_name="goods",
    )
    # lasy import
    book = models.ForeignKey(
        'books.Book',
        on_delete=models.PROTECT,
        verbose_name="Книга"
    )
    quantity = models.IntegerField(
        verbose_name="Количество",
        default=1,

    )
    unit_price = models.DecimalField(verbose_name="Цена", decimal_places=2, max_digits=9)
    created = models.DateTimeField(
        verbose_name="Дата создания",
        auto_now=False, 
        auto_now_add=True)
    updated = models.DateTimeField(
        verbose_name="Дата последнего изменения",
        auto_now=True, 
        auto_now_add=False)

    @property # Декоратор для удобства, чтобы м.б. обращаться как к свойству
    def total_price(self):
        return self.unit_price * self.quantity

# это д.б. в отдельном приложении для заказов
class Order(models.Model):
    cart = ForeignKey(
        Cart,
        on_delete=models.PROTECT,
        verbose_name='Заказ'
    )
    contact_info = models.TextField(verbose_name="Контактная инфорамация")
    created = models.DateTimeField(
        verbose_name="Дата внесения в каталог",
        auto_now=False, 
        auto_now_add=True)
    updated = models.DateTimeField(
        verbose_name="Дата последнего изменения",
        auto_now=True, 
        auto_now_add=False)