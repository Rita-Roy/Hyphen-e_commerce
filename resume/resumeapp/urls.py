from django.urls import path
from resumeapp import views
urlpatterns=[
    path("",views.home),
    path("detailing",views.resume_website)
]