from django.shortcuts import render

rooms = [
    {'id':1, 'name':'Django rocks', 'spiritometer':"enlightened"},
    {'id':2, 'name':'Python Programming', 'spiritometer':"success"},
    {'id':3, 'name':'Javascript is a beast', 'spiritometer':"info"}
]

# Create your views here.
def home(request):
    context = {'rooms':rooms}
    return render(request, 'home.html', context)

def room(request, pk):
    for room in rooms:
        if room['id'] == pk:
            context = {'room': room}
        

    return render(request, 'room.html', context)