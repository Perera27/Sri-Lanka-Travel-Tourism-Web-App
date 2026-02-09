from django.shortcuts import render

def travel_home(request):
    return render(request, "destinations/travel_home.html")
