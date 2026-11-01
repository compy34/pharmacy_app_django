from django.urls import path
from django.contrib.auth import views as auth_views
from .views import *

urlpatterns = [
    path("signin/", auth_views.LoginView.as_view(template_name="accounts/signin.html"), name="login"),
    path("signup/", signup_view, name="signup"),
    path('signout/', auth_views.LogoutView.as_view(), name='logout'),
    path('profile/', profile_view, name='profile'),
]