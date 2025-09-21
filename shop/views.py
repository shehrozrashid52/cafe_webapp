from django.shortcuts import render

def home(request):
    return render(request, "shop/home.html")

def menu(request):
    return render(request, "shop/menu.html")

def find_cafe(request):
    return render(request, "shop/find_cafe.html")

def contact(request):
    return render(request, "shop/contact.html")

def about(request):
    return render(request, "shop/about.html")

def cart(request):
    return render(request, "shop/cart.html")

def checkout(request):
    return render(request, "shop/checkout.html")
