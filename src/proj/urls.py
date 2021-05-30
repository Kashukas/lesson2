"""proj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from manuals import views as manuals_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', manuals_views.main_page, name="main-page"),
    path('author/<int:author_id>/', manuals_views.author_view, name="author"),
    path('authors/', manuals_views.author_list, name="authors"),
    path('serie/<int:serie_id>/', manuals_views.serie_view, name="serie"),
    path('series/', manuals_views.serie_list, name="series"),
    path('genre/<int:genre_id>/', manuals_views.genre_view, name="genre"),
    path('genres/', manuals_views.genre_list, name="genres"),
    path('publisher/<int:publisher_id>/', manuals_views.publisher_view, name="publisher"),
    path('publishers/', manuals_views.publisher_list, name="publishers"),
    path('create-author/', manuals_views.author_create, name="author-create"),
    path('update-author/<int:author_id>', manuals_views.author_update, name="author-update"),
    path('delete-author/<int:author_id>', manuals_views.author_delete, name="author-delete"),
    path('create-serie/', manuals_views.serie_create, name="serie-create"),
    path('update-serie/<int:serie_id>', manuals_views.serie_update, name="serie-update"),
    path('delete-serie/<int:serie_id>', manuals_views.serie_delete, name="serie-delete"),
    path('create-genre/', manuals_views.genre_create, name="genre-create"),
    path('update-genre/<int:genre_id>', manuals_views.genre_update, name="genre-update"),
    path('delete-genre/<int:genre_id>', manuals_views.genre_delete, name="genre-delete"),
    path('create-publisher/', manuals_views.publisher_create, name="publisher-create"),
    path('update-publisher/<int:publisher_id>', manuals_views.publisher_update, name="publisher-update"),
    path('delete-publisher/<int:publisher_id>', manuals_views.publisher_delete, name="publisher-delete"),
]
