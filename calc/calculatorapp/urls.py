from django.urls import path
from calculatorapp import views
urlpatterns=[
    path("",views.home2),
    path("calculating",views.calculation)
    
]