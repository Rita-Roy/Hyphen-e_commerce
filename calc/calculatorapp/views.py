from django.shortcuts import render
from django.http import HttpResponse

def home2(request):
    return render(request,"calcu.html")
def calculation(request):
    num1=int(request.POST["num1"])
    num2=int(request.POST["num2"])
    button=(request.POST["btn"])
    if button=="+":
        result=num1+num2
    elif button=="-":
        result=num1-num2
    elif button=="*":
        result=num1*num2
    elif button=="/":
        result=num1/num2
        
    return render(request,"calcu.html",{"result":result})

# Create your views here.
