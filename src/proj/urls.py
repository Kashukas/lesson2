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
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from manuals import views as manuals_views
from books import views as books_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin1/', admin.site.urls),
    path('author/', include('manuals.urls', namespace='author')),
    path('serie/', include('manuals.urls', namespace="serie")),
    path('genre/', include('manuals.urls', namespace="genre")),
    path('status/', include('manuals.urls', namespace="status")),
    path('publisher/', include('manuals.urls', namespace="publisher")),
    path('cart/', include('carts.urls', namespace="cart")),
    path('book/', include('books.urls', namespace="book")),
    path('admin/', manuals_views.Home.as_view(), name="admin"),
    path('user/', include('users.urls', namespace="user")),
    path('order/', include('orders.urls', namespace="order")),
    path('comment/', include('comments.urls', namespace="comment")),
    path('', books_views.BookListLastView.as_view(), name="main-page"),
]



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)