from django.shortcuts import render                   #use try...except always 
from django.http import HttpResponse
from .models import Employee

def home(request):
    return render(request,"datab.html")

#CRUD

#create
def addemployee(request):
    try:
        Name=request.POST['name']
        Address=request.POST['address']
        Age=int(request.POST['age'])
        image=request.FILES['Image']
        empobj=Employee.objects.create(name=Name,address=Address,age=Age,image=image)
        empobj.save()
        return render(request,'datab.html',{'msg':'Employee added'})
    
    except Exception as e:  #variable e is used to store info about exception
        print(e)   #this will print the error message(exception) to the terminal or console
        return render(request,'datab.html',{"msg":"Employee can't be added"})

# Create your views here.


#read

def display(request):
    empdtls=Employee.objects.all()   #fetching all the employee details onto empdtls
    return render(request,'datab.html',{"emp":empdtls})

#all()-when we nee dto fetch all records(no conditions here)
#get()-single record is only needed to fetch(need to provide condition usually primary key is used)
#filter()-when we need to fetch the records accordng to a conditon(multiple records can be fetched)


#DELETE

def delete(request):
    Name=request.POST['name']
    empdtls=Employee.objects.filter(name=Name)
    #empdtls=Employee.objects.get(id=eid)
    empdtls.delete()
    return render(request,'datab.html',{"msg":"Deleted"})


#UPDATE

def updatename(request):
    oldname=request.POST["oldname"]
    newname=request.POST["newname"]
    emp=Employee.objects.get(name=oldname)
    emp.name=newname
    emp.save()
    return render(request,"datab.html",{"msg":"updated"})


