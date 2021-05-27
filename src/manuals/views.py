from django.shortcuts import render

from . import models
# Create your views here.

def author_view(request, author_id):
    author = models.Author.objects.get(pk=author_id)
    ctx = {
        'author': author
    }
    return render(request, template_name="author_detail.html", context=ctx)

def author_list(request):
    author_list = models.Author.objects.all()
    ctx = {
        'author_list': author_list
    }
    return render(request, template_name="author_list.html", context=ctx)

def serie_view(request, serie_id):
    serie = models.Serie.objects.get(pk=serie_id)
    ctx = {
        'serie': serie
    }
    return render(request, template_name="serie_detail.html", context=ctx)

def serie_list(request):
    serie_list = models.Serie.objects.all()
    ctx = {
        'serie_list': serie_list
    }
    return render(request, template_name="serie_list.html", context=ctx)

def genre_view(request, genre_id):
    genre = models.Genre.objects.get(pk=genre_id)
    ctx = {
        'genre': genre
    }
    return render(request, template_name="genre_detail.html", context=ctx)

def genre_list(request):
    genre_list = models.Genre.objects.all()
    ctx = {
        'genre_list': genre_list
    }
    return render(request, template_name="genre_list.html", context=ctx)

def publisher_view(request, publisher_id):
    publisher = models.Publisher.objects.get(pk=publisher_id)
    ctx = {
        'publisher': publisher
    }
    return render(request, template_name="publisher_detail.html", context=ctx)

def publisher_list(request):
    publisher_list = models.Publisher.objects.all()
    ctx = {
        'publisher_list': publisher_list
    }
    return render(request, template_name="publisher_list.html", context=ctx)
