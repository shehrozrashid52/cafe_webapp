from django.shortcuts import render

def home(request):
    return render(request, 'cafe/home.html')

def menu(request):
    return render(request, 'cafe/menu.html')

def gallery(request):
    return render(request, 'cafe/gallery.html')

def about(request):
    return render(request, 'cafe/about.html')

def contact(request):
    return render(request, 'cafe/contact.html')