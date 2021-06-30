from django.urls import path

from django.contrib.auth import views as auth_views
from users import views as users_views

app_name = 'users'

urlpatterns = [
    path('login/', users_views.UserLoginView.as_view(), name='login'),
    path('chp/', users_views.PwdChangeView.as_view(), name='chp'),
]

#path('chp/', users_views.PasswordChangeView.as_view(template_name="users/pch.html"), name='chp'),