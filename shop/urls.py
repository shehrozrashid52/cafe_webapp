from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('menu/', views.menu, name="menu"),
    path('find-cafe/', views.find_cafe, name="find_cafe"),
    path('contact/', views.contact, name="contact"),
    path('about/', views.about, name="about"),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),
]
