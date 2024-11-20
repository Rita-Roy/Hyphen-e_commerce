from django.urls import path
from quoteapp import views
urlpatterns=[
    path("",views.home),
    path("quoting",views.quotes_pick)
]