from django.shortcuts import render
from django.http import HttpResponse
import random

def home(request):
    return render(request,'quotes.html')
def quotes_pick(request):
    quote= [
     "The greatest glory in living lies not in never falling, but in rising every time we fall."+" ""author: Nelson Mandela",
     "The way to get started is to quit talking and begin doing."+" ""author: Walt Disney",
     "Your time is limited, don't waste it living someone else's life."+" ""author: Steve Jobs",
    "If life were predictable it would cease to be life, and be without flavor."+" ""author: Eleanor Roosevelt",
    "If you look at what you have in life, you'll always have more."+" ""author: Oprah Winfrey"
    ]

    result=random.choice(quote)
    return render(request,"quotes.html",{"result":result})

# Create your views here.

# return render(request,'quotes.html',{"quote":quote['text']+" By "+quote['author'])}