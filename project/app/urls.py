from django.urls import path
from .views import index, filter_products, cart, to_cart, detail

urlpatterns = [
    path('', index, name='index'),
    path('product/<int:id>/', filter_products, name='filter'),
    path('cart/', cart, name='cart'),
    path('to-cart/<int:product_id>/<str:action>/', to_cart, name='to_cart'),
    path('product/<int:id>/', detail, name='detail'),
]