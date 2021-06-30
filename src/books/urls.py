from django.urls import path

from books import views as books_views
from carts import views as carts_views

app_name = 'books'

urlpatterns = [
    path('book/<int:pk>/', books_views.BookDetailView.as_view(), name="book"),
    path('books/', books_views.BookListView.as_view(), name="books"),
    path('create-book/', books_views.BookCreateView.as_view(), name="book-create"),
    path('update-book/<int:pk>', books_views.BookUpdateView.as_view(), name="book-update"),
    path('delete-book/<int:pk>', books_views.BookDeleteView.as_view(), name="book-delete"),
    path('cart', carts_views.CartView.as_view(), name="cart-edit"),
]