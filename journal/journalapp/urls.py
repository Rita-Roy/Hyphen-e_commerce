from django.urls import path
from .import views
urlpatterns=[   path("",views.home,name="home"),
                path("create/service/",views.create_service,name="createservice"),
                path("view/service/",views.view_service,name="viewservice"),
                path("delete/service/",views.delete_service,name="deleteservice"),
             
             
                path("create/hairstylist/",views.create_hairstylist,name="createhairstylist"),
                path("view/hairstylist/",views.view_hairstylist,name="viewhairstylist"),
             
             
                path("create/appointment/",views.create_appointment,name="createappointment"),
                path("view/appointment/",views.view_appointment,name="viewappointment")]