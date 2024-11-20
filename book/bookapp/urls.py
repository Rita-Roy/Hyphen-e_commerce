from django.urls import path
from .import views

urlpatterns=[
    path('books-by-author/<int:author_id>/',views.books_by_uthor)
]