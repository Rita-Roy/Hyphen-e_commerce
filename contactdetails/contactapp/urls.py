from django.urls import path
from contactapp import views
urlpatterns=[
    path("",views.home),
    path("contacting",views.contact_details)

]