from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def home(request):
    return render(request,'registration/index.html')

def signup(request):
    if request.method=="POST":
        username=request.POST['username']  #name= given in the signup.html
        fname=request.POST['fname']
        lname=request.POST['fname']
        email=request.POST['email']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']
        if pass1 != pass2:
            messages.error(request, "Passwords do not match.")
            return render(request, "registration/signup.html")

        myuser=User.objects.create_user(username,email,pass1)
        myuser.first_name=fname
        myuser.last_name=lname

        myuser.save()
        messages.success(request, "Your account has been successfully created")
        return redirect('signin')
    return render(request,"registration/signup.html")

def signin(request):
    if request.method=="POST":
        username=request.POST['username']
        pass1=request.POST["pass1"]
        user=authenticate(username=username, password=pass1)

        if user is not None:
            login(request, user)
            fname=user.first_name
            return render(request,"registration/index.html", {'fname':fname})
    return render(request,"registration/signin.html")

def signout(request):
    logout(request)
    messages.success(request,"Successfully logged out")
    return redirect('signin')