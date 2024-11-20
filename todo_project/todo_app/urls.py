from todo_app import views
from django.urls import path


urlpatterns=[
    path('',views.home),
    path('add/',views.list_add,name="add"),
    path("display/",views.list_display,name="display"),

]