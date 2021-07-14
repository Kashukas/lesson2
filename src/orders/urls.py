from django.urls import path

from . import views

app_name = 'orders'

urlpatterns = [
    path('create-order/', views.CreateOrderView.as_view(), name='create-order'),
    path('order/<int:pk>/', views.OrderDetailView.as_view(), name='order'),
    path('orders/', views.OrderListView.as_view(), name='orders'),
    path('order-delete/<int:pk>/', views.OrderDeleteView.as_view(), name='order-delete'),
    path('order-update/<int:pk>/', views.OrderUpdateView.as_view(), name='order-update'),
]










