from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request,"contact.html")
def contact_details(request):
    name=(request.POST["name"])
    mail=(request.POST["mail"])
    result="Thank you,"+" "+name+" "+"for submitting your email!"
    return render(request,"contact.html",{"result":result})
# Create your views here.
