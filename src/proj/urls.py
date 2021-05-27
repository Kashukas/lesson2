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
    path('author/<int:author_id>/', manuals_views.author_view, name="author"),
    path('authors/', manuals_views.author_list, name="authors"),
    path('serie/<int:serie_id>/', manuals_views.serie_view, name="serie"),
    path('series/', manuals_views.serie_list, name="series"),
    path('genre/<int:genre_id>/', manuals_views.genre_view, name="genre"),
    path('genres/', manuals_views.genre_list, name="genres"),
    path('publisher/<int:publisher_id>/', manuals_views.publisher_view, name="publisher"),
    path('publishers/', manuals_views.publisher_list, name="publishers"),

]
