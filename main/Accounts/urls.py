from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", views.register, name="register"),
    path("Login/", views.login, name="login"),
    path("Logout/", views.logout, name="logout"),
    # path('Login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    # path('Logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
]
