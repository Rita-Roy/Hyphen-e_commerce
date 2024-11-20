from django.urls import path
from wordapp import views
urlpatterns=[
    path("",views.home1),
    path("counting",views.word_count)
]