from django.shortcuts import render, get_object_or_404, redirect
from .models import Movie,Showtime,Seat
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .forms import SignUpForm




def home(request):
    return render(request,"home.html")
def login_user(request):
    if request.method=="POST":  #if they filled out the form do the below things
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request, username=username, password=password)#auhenticating whethere uname and ppass are crct
        if user is not None:
            login(request,user)
            messages.success(request,("You have been logged in"))
            return redirect('home')
        else:
            messages.success(request,("There was an error, please try again"))
            return redirect('login')
        
    else:
        return render(request,'login.html',{})
    

def logout_user(request):
    logout(request)
    messages.success(request,"You have been logged out successfully")
    return redirect('home')

def register_user(request):
    form=SignUpForm() #defining our form
    if request.method=="POST":#if they are filling the form
        form=SignUpForm(request.POST)#all the stuff from for form is inserted to signupform
        if form.is_valid():
            form.save()#saving those data
            username=form.cleaned_data['username'] #taking those information to log in
            password=form.cleaned_data['password1']
            #log in user
            user=authenticate(username=username,password=password)
            login(request, user)
            messages.success(request,("You have registered successfully"))
            return redirect('home')
        else:
            messages.successs(request,("Whoops!, There was a problem while registering, please try again "))
            return redirect('register')
    else:
        return render(request,'register.html',{'form':form})

def upcoming_movies(request):
    return render(request, 'upcoming_movies.html')
def movie_list(request):
    movies=Movie.objects.all()
    return render(request,'movie_list.html',{'movies':movies})

def select_showtime(request, movie_id):  #each movie have an id
    movie=get_object_or_404(Movie,pk=movie_id) #obtaining the movie with the particular movie_id onto the variable movie,if not found 404 error
    showtimes=Showtime.objects.filter(movie=movie)#obtaining the showtime of that particular movie
    if request.method=="POST":
        showtime_id=request.POST.get('showtime') #retreiving showtime from the submitted showtimes
        return redirect('select_seat',showtime_id=showtime_id) #
    return render(request, "select_showtime.html",{"movie":movie,'showtimes':showtimes})
def select_seat(request, showtime_id):
    showtime = get_object_or_404(Showtime, pk=showtime_id)
    seats = Seat.objects.filter(showtime=showtime, is_available=True) #boolean field that only retrieves available seats, retrieves all available seats for the given showtime
    if request.method == "POST": #check whether the form used to select a seat is submitted
        seat_id = request.POST.get('seat')#retrieves the value of the selected seat from the form submitted in the POST request
        selected_seat = get_object_or_404(Seat, pk=seat_id)#retrieves the corresponding Seat object from the database
        selected_seat.is_available = False  # Mark the seat as booked
        selected_seat.save()
        messages.success(request, f"Ticket confirmed for {showtime.movie.title} at {showtime.show_date} {showtime.show_time}!")
        return redirect('select_seat', showtime_id=showtime_id)
    return render(request, 'select_seat.html', {'showtime': showtime, 'seats': seats})
