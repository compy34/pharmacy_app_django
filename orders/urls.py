from django.urls import path

from .views import *

urlpatterns = [
    path('', cart_view, name='cart'),
    path('cart/add/<int:offer_id>', add_to_cart, name='add_to_cart'),
    path('checkout/', checkout, name='checkout'),
    path('my_orders/', my_orders, name='my_orders'),

]