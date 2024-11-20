from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# Create your views here.



@login_required
def home(request):
    return render(request,'auth.html')

def loginview(request):
    uname=request.POST['username']
    pwd=request.POST['password']
    user=authenticate(request,username=uname,password=pwd)#authenticating whether this username and password exists or not
    if user is not None: #if authentication failed it will return None
        login(request, user)   #allows the user to login
        return redirect('home')  #redirection to home page from login page
    else:
        return render(request,'login.html',{"msg":"Invalid login"})
    
def logout_view(request):
    logout(request)  #logout-builtin function
    return redirect('login') #redirecting to login page

def sign_up(request):
    try:
        form=UserCreationForm(request.POST)
        if request.method=="POST":
            if form.is_valid():
                form.save() #auth user (saved here)
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
