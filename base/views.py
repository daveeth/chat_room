from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from .models import Room 

rooms = [
    {'id':1, 'name':'Django rocks', 'spiritometer':"enlightened"},
    {'id':2, 'name':'Python Programming', 'spiritometer':"success"},
    {'id':3, 'name':'Javascript is a beast', 'spiritometer':"info"}
]

# Create your views here.
def home(request):
    rooms = Room.objects.all()
    context = {'rooms':rooms}
    return render(request, 'home.html', context)

def room(request, pk):
    room = get_object_or_404(Room, id=pk)
    msgs = room.message_set.filter(room=room)
    context = {'room':room, 'msgs':msgs}

    return render(request, 'room.html', context)