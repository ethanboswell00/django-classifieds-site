# classifieds/views.py

from django.shortcuts import render

def home(request):
    return render(request, "index.html", {})

def alt_home(request):
    return render(request, "indexv2.html", {})

def err(request):
    return render(request, "404error.html", {})

def about_us(request):
    return render(request, "aboutus.html", {})

def contact_us(request):
    return render(request, "contactus.html", {})

def coming_soon(request):
    return render(request, "comingsoon.html", {})

def packages(request):
    return render(request, "packages.html", {})
