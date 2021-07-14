from django.urls import path

from manuals import views as manuals_views

app_name = 'manuals'

urlpatterns = [
    path('author/<int:pk>/', manuals_views.AuthorDetailView.as_view(), name="author"),
    path('authors/', manuals_views.AuthorListView.as_view(), name="authors"),
    path('create-author/', manuals_views.AuthorCreateView.as_view(), name="author-create"),
    path('update-author/<int:pk>', manuals_views.AuthorUpdateView.as_view(), name="author-update"),
    path('delete-author/<int:pk>', manuals_views.AuthorDeleteView.as_view(), name="author-delete"),
    
    path('serie/<int:pk>/', manuals_views.SerieDetailView.as_view(), name="serie"),
    path('series/', manuals_views.SerieListView.as_view(), name="series"),
    path('create-serie/', manuals_views.SerieCreateView.as_view(), name="serie-create"),
    path('update-serie/<int:pk>', manuals_views.SerieUpdateView.as_view(), name="serie-update"),
    path('delete-serie/<int:pk>', manuals_views.SerieDeleteView.as_view(), name="serie-delete"),
    
    path('genre/<int:pk>/', manuals_views.GenreDetailView.as_view(), name="genre"),
    path('genres/', manuals_views.GenreListView.as_view(), name="genres"),
    path('create-genre/', manuals_views.GenreCreateView.as_view(), name="genre-create"),
    path('update-genre/<int:pk>', manuals_views.GenreUpdateView.as_view(), name="genre-update"),
    path('delete-genre/<int:pk>', manuals_views.GenreDeleteView.as_view(), name="genre-delete"),
    
    path('publisher/<int:pk>/', manuals_views.PublisherDetailView.as_view(), name="publisher"),
    path('publishers/', manuals_views.PublisherListView.as_view(), name="publishers"),
    path('create-publisher/', manuals_views.PublisherCreateView.as_view(), name="publisher-create"),
    path('update-publisher/<int:pk>', manuals_views.PublisherUpdateView.as_view(), name="publisher-update"),
    path('delete-publisher/<int:pk>', manuals_views.PublisherDeleteView.as_view(), name="publisher-delete"),

    path('status/<int:pk>/', manuals_views.StatusDetailView.as_view(), name="status"),
    path('statuses/', manuals_views.StatusListView.as_view(), name="statuses"),
    path('create-status/', manuals_views.StatusCreateView.as_view(), name="status-create"),
    path('update-status/<int:pk>', manuals_views.StatusUpdateView.as_view(), name="status-update"),
    path('delete-status/<int:pk>', manuals_views.StatusDeleteView.as_view(), name="status-delete"),
]