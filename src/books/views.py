from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.db.models import Q

from . import models
from . import forms

# Create your views here.

class BookDetailView(DetailView):
    model = models.Book

class BookListView(ListView):
    model = models.Book
    paginate_by = 5
    # Filter books list:
    def get_queryset(self):
        qs = super().get_queryset()
        filter = self.request.GET.get('filter')
        search_data = self.request.GET.get('search_data') # Данные введенные в окне 'Поиск'
        if filter == 'av':
            return qs.filter(active=True)
        if filter == 'not_av':
            return qs.filter(active=False)
        if search_data:
            return qs.filter(Q(name__icontains=search_data) | Q(author__name__icontains=search_data)) # Условие или - |
        return qs

class BookCreateView(CreateView):
    model = models.Book
    form_class = forms.CreateBookForm # или сослаться на форму
    template_name = "books/book_create.html"

class BookUpdateView(UpdateView):
    model = models.Book
    form_class = forms.CreateBookForm
    template_name = "books/book_create.html"

class BookDeleteView(DeleteView):
    model = models.Book
    success_url = reverse_lazy('book:books')

class BookListLastView(ListView):
    template_name = "books/book_home.html"
    model = models.Book
    def get_context_data(self, **kwargs):
        list_last = models.Book.objects.order_by('-created')[0:3]
        list_best = models.Book.objects.order_by('-rating')[0:3] 
        context = super().get_context_data(**kwargs)
        context['list_last'] = list_last
        context['book_1'] = list_last[0]
        context['book_2'] = list_last[1]
        context['book_3'] = list_last[2]
        context['list_best'] = list_best
        context['book_b_1'] = list_best[0]
        context['book_b_2'] = list_best[1]
        context['book_b_3'] = list_best[2]
        return context

class BookListBestView(ListView):
    set = [1, 2, 3]
    template_name = "books/book_home.html"
    model = models.Book
    def get_context_data(self, **kwargs):
        list_last = models.Book.objects.order_by('-created')[0:3]
        context = super().get_context_data(**kwargs)
        context['list_last'] = list_last
        context['book_1'] = list_last[0]
        context['book_2'] = list_last[1]
        context['book_3'] = list_last[2]
        return context