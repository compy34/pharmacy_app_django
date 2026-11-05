from django.urls import path

from .views import home_view, about_view, list_view, details_view

urlpatterns = [
    path('', home_view, name='home'),
    path('about', about_view, name='about'),
    path('list', list_view, name='list'),
    path('<int:pk>', details_view, name='details'),
]