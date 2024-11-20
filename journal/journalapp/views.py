from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Hairstyle, Hairstylist, Appointment
from .forms import HairstyleForm, HairstylistForm, AppointmentForm


def home(request):
    return render(request,"home.html")


def create_service(request):
    if request.method == 'POST':
        form = HairstyleForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Hairstyle added successfully!")
            return redirect('service_list')  
    else:
        form = HairstyleForm()
    return render(request, 'create_service.html', {'form': form})
def delete_service(request):
    Name=request.POST["name"]
    emp=Hairstyle.objects.all(name=Name)
    emp.delete()
    return render(request,"home.html",{"msg":"deleted"})



def view_service(request):
    hairstyles = Hairstyle.objects.all() 
    return render(request, 'service.html', {'hairstyles': hairstyles})


def create_hairstylist(request):
    if request.method == 'POST':
        form = HairstylistForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Hairstylist added successfully!")
            return redirect('hairstylist')  
    else:
        form = HairstylistForm()
    return render(request, 'create_hairstylist.html', {'form': form})


def view_hairstylist(request):
    hairstyles = Hairstylist.objects.all() 
    return render(request, 'hairstylist.html', {'hairstyles': hairstyles})



def create_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Appointment added successfully!")
            return redirect('home')  
    else:
        form = AppointmentForm()
    return render(request, 'create_appointment.html', {'form': form})



def view_appointment(request):
    hairstyles = Appointment.objects.all() 
    return render(request, 'appointment.html', {'hairstyles':hairstyles})
