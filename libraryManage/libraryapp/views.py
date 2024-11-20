from django.shortcuts import render
from django.http import HttpResponse
from .forms import LibraryForm
from .models import Library


# Create your views here.
def home(request):
    libform=LibraryForm()
    return render(request,"lib.html",{'form':libform})

def addbook(request):

    try:
        if request.method=="POST":
            libform=LibraryForm(request.POST)
            if libform.is_valid():
                libform.save()
        return render(request,'lib.html',{'form':libform,"msg":"Book Added"})
    
    except Exception as e:
        print(e)
        return HttpResponse("Error")
    

#update

def updatebook(request):
    oldauthor=request.POST['oldauthor']
    newauthor=request.POST['newauthor']
    libr=Library.objects.filter(author=oldauthor)
    libr.author=newauthor
    libr.save()
    return render(request,'lib.html',{'msg':"updated"})


#delete

def delete(request):
    Author=request.POST['author']
    libr=Library.objects.filter(author=Author)
    libr.delete()
    return render(request,"lib.html",{"msg":"Deleted"})

def display(request):
    libr=Library.objects.all()
    return render(request,"lib.html",{'lib':libr})


def search(request):
    title=request.POST.get("title")
    author=request.POST.get('author')
    libr=Library.objects.filter(title__icontains=title,author__icontains=author)
    return render(request,"lib.html",{'libr':libr})