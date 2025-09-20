from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("menu/", views.menu, name="menu"),
    path("find-cafe/", views.find_cafe, name="find_cafe"),  
    path("contact/", views.contact, name="contact"),
]
