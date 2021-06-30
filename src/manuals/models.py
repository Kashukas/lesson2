from django.db import models
from django.db.models.base import Model


from django.urls import reverse
# Create your models here.

class Author(models.Model):
    name = models.CharField(verbose_name="Автор", max_length=200)
    description = models.TextField(verbose_name= "Краткое описание", default="Описание отсутствует")

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):
        return reverse('author:authors') #args=[self.pk]

    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"


class Serie(models.Model):
    bookserie = models.CharField(verbose_name="Серия книг", max_length=100, null=True, blank=True)
    books_quantity = models.IntegerField(verbose_name="Количество книг в серии", blank=True, null=True)

    def __str__(self) -> str:
        return self.bookserie

    def get_absolute_url(self):
        return reverse('serie:series')

    class Meta:
        verbose_name = "Серия"
        verbose_name_plural = "Серии"


class Genre(models.Model):
    genre_name = models.CharField(verbose_name="Название жанра", max_length=100)
    description = models.TextField(verbose_name="Описание жанра", default="Описание отсутствует")

    def __str__(self) -> str:
        return self.genre_name

    def get_absolute_url(self):
        return reverse('genre:genres')

    class Meta:
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"


class Publisher(models.Model):
    publisher_name = models.CharField(verbose_name="Издательство", max_length=100)

    def __str__(self) -> str:
        return self.publisher_name
    
    def get_absolute_url(self):
        return reverse('publisher:publishers')

    class Meta:
        verbose_name = "Издатель"
        verbose_name_plural = "Издатели"

class Status(models.Model):
    order_status = models.CharField(verbose_name="Статус заказа", max_length=100)

    def __str__(self) -> str:
        return self.order_status
    
    def get_absolute_url(self):
        return reverse('status:statuses')

    class Meta:
        verbose_name = "Статус заказа"
        verbose_name_plural = "Статусы заказов"