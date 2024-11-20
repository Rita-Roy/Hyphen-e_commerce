from django.shortcuts import render
from .forms import MyForm


def home_view(request):
    form=MyForm()
    return render(request, "form.html",{"form":form})
def showdetails(request):
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():                             
            Name = form.cleaned_data['name']    
            Address = form.cleaned_data['address']   
            Age = form.cleaned_data['age']           
            Phoneno = form.cleaned_data['phoneno']   
            return render(request, "success.html", {'msg':"Submitted Successfuly",
                'name': Name,
                'address': Address,
                'age': Age,
                'phoneno': Phoneno})
        
        else:
            return render(request, "form.html", {'form': form})

    else:
        form = MyForm()
        return render(request, "form.html",{'form': form})

# Create your views here.
