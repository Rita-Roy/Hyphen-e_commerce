from django.urls import path
from libraryapp import views
urlpatterns=[
    path("",views.home),
    path("add",views.addbook),
    path("update",views.updatebook),
    path("delete",views.delete),
    path("display",views.display),
    path("search",views.search)
] 