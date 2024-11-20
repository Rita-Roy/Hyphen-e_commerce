from django import forms
from .models import Hairstylist, Hairstyle, Appointment
from django.contrib.auth.models import User

class HairstylistForm(forms.ModelForm):
    class Meta:
        model = Hairstylist
        fields ="__all__"
        
class HairstyleForm(forms.ModelForm):
    class Meta:
        model = Hairstyle
        fields = "__all__"
    
          

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields='__all__'