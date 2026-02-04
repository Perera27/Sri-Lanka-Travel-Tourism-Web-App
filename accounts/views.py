from django.shortcuts import render

def home(request):
    return render(request, "home.html")

def register_page(request):
    return render(request, "accounts/register.html")
