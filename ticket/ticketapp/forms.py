from django import forms
from .models import Movie,ShowTime,Seat


class MovieForm(forms.ModelForm):
    class Meta:
        model=Movie
        fields="__all__"

class ShowTimeForm(forms.ModelForm):
    class Meta:
        model=ShowTime
        fields="__all__"

class SeatForm(forms.ModelForm):
    class Meta:
        model=Seat
        fields="__all__"

