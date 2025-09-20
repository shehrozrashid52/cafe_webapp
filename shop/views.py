from django.shortcuts import render

def home(request):
    return render(request, "shop/home.html")

def menu(request):
    return render(request, "shop/menu.html")

def find_cafe(request):
    return render(request, "shop/find_cafe.html")

def contact(request):
    return render(request, "shop/contact.html")  