from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from . import models
from . import forms
# Create your views here.

# Author V(l)
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
# End of Author V(l)

# Serie V(l)
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
# End of Serie V(l)

# Genre V(l)
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
# End of Genre V(l)

# Publisher V(l)
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
# End of Publisher V(l)

def main_page(request):
    return render(request, template_name="main_page.html", context={})

# Lesson 17
# Author CUD
def author_create(request):
    if request.method == 'POST':
        form = forms.CreateAuthorForm(request.POST)
        if form.is_valid():
            form.save()
            #print(form.cleaned_data)
            #author_name = form.cleaned_data.get()
            #obj = models.Author.objects.create(name=name, description=description)
            return HttpResponseRedirect(reverse("authors"))
        else:
            pass
        #name = request.POST.get('name')
        #description = request.POST.get('description')
    else:
        form = forms.CreateAuthorForm()
    #print(name, description)
    #obj = models.Author.objects.create(name=name, description=description)
    #author_create = models.Publisher.objects.all()
    ctx = {
        'form': form,
        'is_valid': form.is_valid()
    }
    return render(request, template_name="author_create.html", context=ctx)


def author_update(request, author_id):
    if request.method == 'POST':
        obj = models.Author.objects.get(pk=author_id)
        form = forms.CreateAuthorForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("authors"))
        else:
            pass
    else:
        obj = models.Author.objects.get(pk=author_id)
        form = forms.CreateAuthorForm(instance=obj)
    ctx = {
        'form': form,
        'is_valid': form.is_valid()
    }
    return render(request, template_name="author_create.html", context=ctx)

def author_delete(request, author_id):
    if request.method == 'POST':
        obj = models.Author.objects.get(pk=author_id).delete()
        return HttpResponseRedirect(reverse("authors"))
    else:
        author = models.Author.objects.get(pk=author_id)
        ctx = {
        'author': author
        }
        return render(request, template_name="author_delete.html", context=ctx)
# End of Author CUD

# Serie CUD
def serie_create(request):
    if request.method == 'POST':
        form = forms.CreateSerieForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("series"))
        else:
            pass
    else:
        form = forms.CreateSerieForm()
    ctx = {
        'form': form,
        'is_valid': form.is_valid()
    }
    return render(request, template_name="serie_create.html", context=ctx)


def serie_update(request, serie_id):
    if request.method == 'POST':
        obj = models.Serie.objects.get(pk=serie_id)
        form = forms.CreateSerieForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("series"))
        else:
            pass
    else:
        obj = models.Serie.objects.get(pk=serie_id)
        form = forms.CreateSerieForm(instance=obj)
    ctx = {
        'form': form,
        'is_valid': form.is_valid()
    }
    return render(request, template_name="serie_create.html", context=ctx)

def serie_delete(request, serie_id):
    if request.method == 'POST':
        obj = models.Serie.objects.get(pk=serie_id).delete()
        return HttpResponseRedirect(reverse("series"))
    else:
        serie = models.Serie.objects.get(pk=serie_id)
        ctx = {
        'serie': serie
        }
        return render(request, template_name="serie_delete.html", context=ctx)
# End of Serie CUD

# Genre CUD
def genre_create(request):
    if request.method == 'POST':
        form = forms.CreateGenreForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("genres"))
        else:
            pass
    else:
        form = forms.CreateGenreForm()
    ctx = {
        'form': form,
        'is_valid': form.is_valid()
    }
    return render(request, template_name="genre_create.html", context=ctx)


def genre_update(request, genre_id):
    if request.method == 'POST':
        obj = models.Genre.objects.get(pk=genre_id)
        form = forms.CreateGenreForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("genres"))
        else:
            pass
    else:
        obj = models.Genre.objects.get(pk=genre_id)
        form = forms.CreateGenreForm(instance=obj)
    ctx = {
        'form': form,
        'is_valid': form.is_valid()
    }
    return render(request, template_name="genre_create.html", context=ctx)

def genre_delete(request, genre_id):
    if request.method == 'POST':
        obj = models.Genre.objects.get(pk=genre_id).delete()
        return HttpResponseRedirect(reverse("genres"))
    else:
        genre = models.Genre.objects.get(pk=genre_id)
        ctx = {
        'genre': genre
        }
        return render(request, template_name="genre_delete.html", context=ctx)
# End of Genre CUD

# Publisher CUD
def publisher_create(request):
    if request.method == 'POST':
        form = forms.CreatePublisherForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("publishers"))
        else:
            pass
    else:
        form = forms.CreatePublisherForm()
    ctx = {
        'form': form,
        'is_valid': form.is_valid()
    }
    return render(request, template_name="publisher_create.html", context=ctx)


def publisher_update(request, publisher_id):
    if request.method == 'POST':
        obj = models.Publisher.objects.get(pk=publisher_id)
        form = forms.CreatePublisherForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("publishers"))
        else:
            pass
    else:
        obj = models.Publisher.objects.get(pk=publisher_id)
        form = forms.CreatePublisherForm(instance=obj)
    ctx = {
        'form': form,
        'is_valid': form.is_valid()
    }
    return render(request, template_name="publisher_create.html", context=ctx)

def publisher_delete(request, publisher_id):
    if request.method == 'POST':
        obj = models.Publisher.objects.get(pk=publisher_id).delete()
        return HttpResponseRedirect(reverse("publishers"))
    else:
        publisher = models.Publisher.objects.get(pk=publisher_id)
        ctx = {
        'publisher': publisher
        }
        return render(request, template_name="publisher_delete.html", context=ctx)
# End of Publisher CUD