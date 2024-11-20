from django.shortcuts import render
from django.http import HttpResponse

def home1(request):
    return render(request,"word1.html")
def word_count(request):
    list1=[]
    txt=(request.POST["txt"])
    list1=txt.split()
    result=len(list1)
    return render(request,"word1.html",{"result":result})

# Create your views here.