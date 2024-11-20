from django.urls import path
from modelFormapp import views
urlpatterns=[
    path("",views.index),
    path("add",views.addcustomer)
]