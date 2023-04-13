from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),
    path('product/product_content_1/', views.product_content_1, name="product_content_1"),
]