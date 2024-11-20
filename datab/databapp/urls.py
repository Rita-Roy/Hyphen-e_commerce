from django.urls import path
from databapp import views

urlpatterns=[
    path("",views.home),
    path('add',views.addemployee,name='addemp'),
    path('read',views.display),
    path('delete',views.delete),
    path("update",views.updatename)
]