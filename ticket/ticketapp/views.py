from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render,redirect,get_object_or_404
from .models import Movie,ShowTime,Seat
from django.contrib import messages
from .forms import MovieForm,ShowTimeForm,SeatForm



# Create your views here.



@login_required
def home(request):
    homeform=MovieForm()
    return render(request,'auth.html',{'homeform': homeform})

def loginview(request):
    uname=request.POST['username']
    pwd=request.POST['password']
    user=authenticate(request,username=uname,password=pwd)#authenticating whether this username and password exists or not
    if user is not None: #if authentication failed it will return None
        login(request, user)   #allows the user to login
        return redirect('movie_list')  #redirection to home page from login page
    else:
        return render(request,'login.html',{"msg":"Invalid login"})
    return render(request,'login.html')
    
def logout_view(request):
    logout(request)  #logout-builtin function
    return redirect('home') #redirecting to login page

def sign_up(request):
    try:
        
        if request.method=="POST":
            form=UserCreationForm(request.POST)
            if form.is_valid():
                form.save() #auth user (saved here)
                messages.success(request,"Registration successfull. Please log in again")
                return redirect('login')
            return render(request,"sign_up.html",{'form':form,'msg':'Invald login'})
        
        else:
            form=UserCreationForm()
        return render(request,'sign_up.html',{'form':form,"msg":'Invalid submission'})
    except Exception as e:
        print(e)
        form=UserCreationForm()
        return render(request,'sign_up.html',{'form':form})
    

def reset_home(request):
    return render(request,"passregister.html")

def resetpassword(request):
    uname=request.POST['uname']
    newpwd=request.POST['password']
    try:
        user=User.objects.get(username=uname)
        if user is not None:
            user.set_password(newpwd)
            user.save()
            return render(request,'passregister.html',{"msg":"Password reset successfully"})
    except Exception as e:
        print(e)
        return render(request,'passregister.html',{"msg":"Failed password reset"})




@login_required
def movie_list(request):
    movies=Movie.objects.all()  #to get all movies from the database
    filmform = MovieForm()
    try:
        
        if request.method=="POST":
            filmform=MovieForm(request.POST)
            if filmform.is_valid():
                filmform.save()
                messages.success(request, "Movie created successfully.")
                return redirect('movie_list') 
            else:
                messages.error(request,"There was an error while adding movie")
        return render(request, 'movielist.html', {'movies': movies, 'form': filmform})
    except Exception as e:
        print(e)
        return HttpResponse('error')

    

@login_required
def showtime_list(request, movie_id):
    selected_movie=get_object_or_404(Movie, id=movie_id) #get the movie or 404 not found retreiving the movie by id
    available_showtimes=ShowTime.objects.filter(movie=selected_movie) #getting the showtime for the selected movie(fetching all the details associted to that movie)
    try:
        showform=ShowTimeForm(initial={'movie': selected_movie})
        if request.method=="POST":
            showform=ShowTimeForm(request.POST)
            if showform.is_valid():
                new_showtime = showform.save(commit=False)
                new_showtime.movie = selected_movie
                new_showtime.save()
                messages.success(request, "Showtime created successfully.")
                return redirect("showtime_list",movie_id=movie_id)

            else:
                messages.error(request,"There was an error while selecting movie")
        return render(request,'showtime_list.html',{'movie':selected_movie,'showtimes': available_showtimes,'form':showform})
    except Exception as e:
        print(e)
        return HttpResponse("error")
    


@login_required
def seat_selection(request, movie_id, showtime_id):
    movie = get_object_or_404(Movie, id=movie_id)  # Fetch the specific movie
    showtime = get_object_or_404(ShowTime, id=showtime_id, movie=movie)  # Fetch the showtime for this movie
    seats = Seat.objects.filter(showtime=showtime)  # Filter seats for this showtime

    if request.method == "POST":
        selected_seat_number = request.POST.get("seat_number")
        if selected_seat_number:
            seat = get_object_or_404(Seat, showtime=showtime, seat_number=selected_seat_number)
            
            if seat.status == 'available':
                seat.status = 'booked'
                seat.save()
                messages.success(request, f"Booking successful for {movie.title} - Seat {seat.seat_number}.")
                return redirect('seat_selection', movie_id=movie.id, showtime_id=showtime.id)
            else:
                messages.error(request, "Selected seat is already booked.")
        else:
            messages.error(request, "No seat selected.")

    return render(request, 'seat_selection.html',{
        'movie': movie,
        'showtime': showtime,
        'seats':seats
})
