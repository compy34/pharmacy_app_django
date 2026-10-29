from django.urls import path

from medicines import views

urlpatterns = [
    path('', views.home, name='home'),
]