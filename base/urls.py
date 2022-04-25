from django.urls import path, include
from django.http import HttpResponse as Http
from .views import home, room

urlpatterns = [
    path('', home, name="home"),
    path('room/<int:pk>', room, name="room"),
]