from django.contrib.auth import login
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views.generic import TemplateView
from django.contrib.auth.mixins import PermissionRequiredMixin, UserPassesTestMixin


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
# End of Publisher CRUD(l)

class Home(PermissionRequiredMixin, TemplateView):
    #units = [1, 2, 3]
    template_name = "manuals/admin_page.html"
    permission_required = 'books.add_book'
    login_url = 'user:login'
    # def test_func(self):
    #     print(self.request.user.groups)
    #     return self.request.user.groups.__contains__('Managers')

    #def get_context_data(self, **kwargs):
    #    list_a = models.Author.objects.all()
    #    list_b = models.Serie.objects.all()
    #    context = super().get_context_data(**kwargs)
    #    context['units'] = self.units
    #    context['list_a'] = list_a
    #    context['list_b'] = list_b
    #    return context

# Start of Status CRUD(l)
class StatusDetailView(DetailView):
    model = models.Status

class StatusListView(ListView):
    model = models.Status

class StatusCreateView(CreateView):
    model = models.Status
    form_class = forms.CreateStatusForm # Ссылка на форму.
    template_name = "manuals/status_create.html"

class StatusUpdateView(UpdateView):
    model = models.Status
    form_class = forms.CreateStatusForm
    template_name = "manuals/status_create.html"

class StatusDeleteView(DeleteView):
    model = models.Status
    success_url = reverse_lazy('status:Statuses')
# End of Status CRUD(l)