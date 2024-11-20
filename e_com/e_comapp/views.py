from django.shortcuts import render, redirect
from .models import Product,Category
from django.contrib.auth import authenticate, logout,login
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm 
from django import forms
from .forms import SignUpForm


def category(request,foo):
    #replace hyphens with spaces
    foo=foo.replace('-'," ")
    #grab category from url
    try:
        #look up the category
        category=Category.objects.get(name=foo)
        products=Product.objects.filter(category=category)
        return render(request,'category.html',{'products':products,'category':category})

    except:
        messages.success(request,("That category doesn't exists"))
        return redirect('home')

def product(request,pk):
    product=Product.objects.get(id=pk)
    return render(request,'product.html',{'product':product})

def home(request):
    products=Product.objects.all()
    return render(request,'home.html',{"products":products})

def about(request):
    return render(request,'about.html',{})
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
