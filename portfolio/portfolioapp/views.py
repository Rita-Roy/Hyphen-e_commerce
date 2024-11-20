from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request,"portfolio.html")
def my_portfolio(request):
    name=(request.POST["name"])
    contact_info=(request.POST["contact_info"])
    mail_id=(request.POST["mail_id"])
    skills=(request.POST["skills"])
    projects=(request.POST["projects"])
    experience=(request.POST["experience"])

    return render(request, "portfolio.html", {
    "name": name,
    "contact_info": contact_info,
    "mail_id": mail_id,
    "skills": skills,
    "projects": projects,
    "experience": experience
    })

# Create your views here.
