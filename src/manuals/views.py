from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views.generic import TemplateView

from . import models
from . import forms

# Create your views here.

# Author CRUD(l)
class AuthorDetailView(DetailView):
    model = models.Author

class AuthorListView(ListView):
    model = models.Author

    # Можно фильтровать данные:
    #def get_queryset(self):
    #    qs = super().get_queryset()
    #    return qs.filter(name= '')
    
    # Если имя шаблона по умолчанию не устраивает, то можно задать самому:
    #template_name = "manuals/author_list.html"

class AuthorCreateView(CreateView):
    model = models.Author
    # или указать поля формы
    #fields = (
    #    'name',
    #    'description',
    #)
    form_class = forms.CreateAuthorForm # или сослаться на форму
    template_name = "manuals/author_create.html"

class AuthorUpdateView(UpdateView):
    model = models.Author
    form_class = forms.CreateAuthorForm
    template_name = "manuals/author_create.html"

class AuthorDeleteView(DeleteView):
    model = models.Author
    success_url = reverse_lazy('author:authors')

# End of Author CRUD(l)

# Serie CRUD(l)
class SerieDetailView(DetailView):
    model = models.Serie

class SerieListView(ListView):
    model = models.Serie

class SerieCreateView(CreateView):
    model = models.Serie
    form_class = forms.CreateSerieForm # Ссылка на форму.
    template_name = "manuals/serie_create.html"

class SerieUpdateView(UpdateView):
    model = models.Serie
    form_class = forms.CreateSerieForm
    template_name = "manuals/serie_create.html"

class SerieDeleteView(DeleteView):
    model = models.Serie
    success_url = reverse_lazy('serie:series')
# End of Serie CRUD(l)

# Genre CRUD(l)
class GenreDetailView(DetailView):
    model = models.Genre

class GenreListView(ListView):
    model = models.Genre

class GenreCreateView(CreateView):
    model = models.Genre
    form_class = forms.CreateGenreForm # Ссылка на форму.
    template_name = "manuals/genre_create.html"

class GenreUpdateView(UpdateView):
    model = models.Genre
    form_class = forms.CreateGenreForm
    template_name = "manuals/genre_create.html"

class GenreDeleteView(DeleteView):
    model = models.Genre
    success_url = reverse_lazy('genre:genres')
# End of Genre CRUD(l)

# Publisher CRUD(l)
class PublisherDetailView(DetailView):
    model = models.Publisher

class PublisherListView(ListView):
    model = models.Publisher

class PublisherCreateView(CreateView):
    model = models.Publisher
    form_class = forms.CreatePublisherForm # Ссылка на форму.
    template_name = "manuals/publisher_create.html"

class PublisherUpdateView(UpdateView):
    model = models.Publisher
    form_class = forms.CreatePublisherForm
    template_name = "manuals/publisher_create.html"

class PublisherDeleteView(DeleteView):
    model = models.Publisher
    success_url = reverse_lazy('publisher:publishers')


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
# End of Publisher CRUD(l)

#def main_page(request): # можно удалить (старая реализация)
#    return render(request, template_name="main_page.html", context={})

class Home(TemplateView):
    # units = [1, 2, 3]
    template_name = "manuals/main_page.html"

    #def get_context_data(self, **kwargs):
    #    list_a = models.Author.objects.all()
    #    list_b = models.Serie.objects.all()
    #    context = super().get_context_data(**kwargs)
    #    context['units'] = self.units
    #    context['list_a'] = list_a
    #    context['list_b'] = list_b
    #    return context

# Lesson 17

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