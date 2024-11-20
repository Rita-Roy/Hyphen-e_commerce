from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request,"resume.html")
def resume_website(request):
    name=(request.POST["name"])
    experience=(request.POST["experience"])
    education=(request.POST["education"])
    skills=(request.POST["skills"])
    contact_info=int(request.POST["contact_info"])

    return render(request,"result.html",({"name":name,"experience":experience,"education":education,"skills":skills,"contact_info":contact_info}))

    


# Create your views here.
