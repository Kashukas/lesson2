from django.db import models
from django.db.models.base import Model

# Create your models here.

class Author(models.Model):
    name = models.CharField(verbose_name="Автор", max_length=200)
    description = models.TextField(verbose_name= "Краткое описание", default="Описание отсутствует")

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"


class Serie(models.Model):
    bookserie = models.CharField(verbose_name="Серия книг", max_length=100, null=True, blank=True)
    books_quantity = models.IntegerField(verbose_name="Количество книг в серии", blank=True, null=True)

    def __str__(self) -> str:
        return self.bookserie

    class Meta:
        verbose_name = "Серия"
        verbose_name_plural = "Серии"


class Genre(models.Model):
    genre_name = models.CharField(verbose_name="Название жанра", max_length=100)
    description = models.TextField(verbose_name="Описание жанра", default="Описание отсутствует")

    def __str__(self) -> str:
        return self.genre_name

    class Meta:
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"


class Publisher(models.Model):
    publisher_name = models.CharField(verbose_name="Издательство", max_length=100)

    def __str__(self) -> str:
        return self.publisher_name

    class Meta:
        verbose_name = "Издатель"
        verbose_name_plural = "Издатели"


#class Book(models.Model):
    #author
    #serie
    #genre
    #publisher

class Meta:
    verbose_name = "Автор"
    verbose_name_plural = "Авторы"
