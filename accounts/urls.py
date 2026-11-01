from django.urls import path

from .views import *

urlpatterns = [
    path("signin", signin_view),
    path("signup", signup_view),
    path('signout', signout_view),
    path('profile', profile_view),
]