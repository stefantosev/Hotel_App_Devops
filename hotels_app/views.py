from django.shortcuts import render, redirect

from hotels_app.forms import ReservationForm, RoomForm
from hotels_app.models import *

# Create your views here.

def index(request):
    rooms = Room.objects.all()
    return render(request, "index.html", {"rooms": rooms})


def add_room(request):
    if request.method == "POST":
        form = RoomForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = RoomForm()

    return render(request, "add_room.html", {"form": form})



def add_reservation(request):
    if request.method == "POST":
        form = ReservationForm(request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ReservationForm()

    return render(request, "add_reservation.html", {"form": form})


def details(request, room_id):
    room = Room.objects.get(id=room_id)
    return render(request, "details.html", {"room": room})

def delete_room(request, room_id):
    room = Room.objects.get(id=room_id)
    room.delete()
    return redirect('index')


def edit_reservation(request, room_id):
    room = Room.objects.get(id=room_id)
