from django.urls import path
from .views import travel_home

urlpatterns = [
    path("", travel_home, name="home"),
    path("travel/", travel_home, name="travel_home"),
]
