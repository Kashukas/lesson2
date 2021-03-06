from django.urls import path

from users import views as users_views

app_name = 'users'

urlpatterns = [
    path('login/', users_views.UserLoginView.as_view(), name='login'),
    path('logout/', users_views.UserLogoutView.as_view(), name='logout'),
    path('chp/', users_views.PwdChangeView.as_view(), name='chp'),
    path('register/', users_views.RegisterView.as_view(), name='register'),
    path('update/<int:pk>/', users_views.UserUpdateView.as_view(), name='update'),
    path('user/<int:pk>/', users_views.UserDetailView.as_view(), name="user"),
    path('users/', users_views.UserListView.as_view(), name="users"),
    path('delete-user/<int:pk>/', users_views.UserDeleteView.as_view(), name="delete-user"),
    path('profile-user/<int:pk>/', users_views.UserProfileView.as_view(), name="profile-user"),

    path('group/<int:pk>/', users_views.GroupDetailView.as_view(), name="group"),
    path('groups/', users_views.GroupListView.as_view(), name="groups"),
    path('group-create/', users_views.GroupCreateView.as_view(), name="group-create"),
    path('group-update/<int:pk>/', users_views.GroupUpdateView.as_view(), name="group-update"),
    path('group-delete/<int:pk>/', users_views.GroupDeleteView.as_view(), name="group-delete"),


]

#path('chp/', users_views.PasswordChangeView.as_view(template_name="users/pch.html"), name='chp'),