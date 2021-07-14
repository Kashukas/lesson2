#from typing_extensions import ParamSpecArgs
from django.db import models

from django.urls import reverse

from manuals.models import Author, Serie, Genre, Publisher
from django.utils.translation import gettext_lazy as _
from comments.models import Comment
from django.contrib.contenttypes.fields import GenericRelation
# Create your models here.

class Book(models.Model):
    class BookRaiting(models.IntegerChoices):
        ONE = 1, _('1')
        TWO = 2, _('2')
        THREE = 3, _('3')
        FOUR = 4, _('4')
        FIVE = 5, _('5')
        __empty__ = _('---')
    
    class BookBinding(models.IntegerChoices):
        HARD = 1, _('Твердый переплет')
        SOFT = 2, _('Мягкий переплет')
        __empty__ = _('---')

    class BookAgeRating(models.IntegerChoices):
        under6 = 1, _('0+')
        after6 = 2, _('6+')
        after12 = 3, _('12+')
        after16 = 4, _('16+')
        after18 = 5, _('18+')
        __empty__ = _('---')


    name = models.CharField(verbose_name="Название книги", max_length=300)
    pic = models.ImageField(
        verbose_name="Обложка книги",
        upload_to='books/%Y/%m/%d/')
    price = models.DecimalField(verbose_name="Цена", decimal_places=2, max_digits=9)
    author = models.ManyToManyField(
        Author,
        related_name='author_books', 
        verbose_name="Автор")
    serie = models.ForeignKey(
        Serie, 
        on_delete=models.PROTECT, 
        related_name='serie_books', 
        verbose_name="Серия книг")
    genre = models.ForeignKey(
        Genre, 
        on_delete=models.PROTECT, 
        related_name='genre_books', 
        verbose_name="Жанр")
    year = models.IntegerField(verbose_name="Год издания")
    pages = models.IntegerField(verbose_name="Количество страниц")
    binding = models.IntegerField(verbose_name="Переплет", choices=BookBinding.choices, default=None)
    format = models.CharField(verbose_name="Формат", max_length=300)
    isbn = models.CharField(verbose_name="ISBN", max_length=20)
    weight = models.IntegerField(verbose_name="Вес книги")
    age_rating = models.IntegerField(verbose_name="Возрастные ограничения", choices=BookAgeRating.choices, default=None)
    publisher = models.ForeignKey(
        Publisher, 
        on_delete=models.PROTECT, 
        related_name='publisher_books', 
        verbose_name="Издатель")
    avail_quan = models.IntegerField(verbose_name="Количество книг в наличии")
    active = models.BooleanField(verbose_name="Доступно для заказа", default=False)
    rating = models.IntegerField(verbose_name="Рейтинг книги", choices=BookRaiting.choices, default=None)
    created = models.DateTimeField(
        verbose_name="Дата внесения в каталог",
        auto_now=False, 
        auto_now_add=True)
    updated = models.DateTimeField(
        verbose_name="Дата последнего изменения",
        auto_now=True, 
        auto_now_add=False)
    description = models.TextField(verbose_name= "Краткое описание", default="Описание отсутствует")
    comment = GenericRelation(Comment)


    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):
        return reverse('book:books') #args=[self.pk]

    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"