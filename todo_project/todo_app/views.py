from django.http import HttpResponse
from django.shortcuts import render
from .models import Task

# Create your views here.
def home(request):
    return render(request,'list.html')

#create......

def list_add(request):
    if request.method=='POST':
        try:
            Tasks=request.POST.get('task_name')
            Current_status=request.POST.get("completion_status")
            Due=request.POST.get('due_date')
            task_obj=Task.objects.create(task_name=Tasks,completion_status=Current_status,due_date=Due)
            task_obj.save()
            return render(request,'list.html',{'msg':"New Task added successfully"})
        except Exception as e:
            print(e)
            return render(request,'list.html',{"msg":"Task can't be added"})
    else:
        return render(request, 'list.html', {"msg": "Invalid request"})
    

#display....

def list_display(request):
    list_details=Task.objects.all()
    return render(request,'list.html',{'todo':list_details})