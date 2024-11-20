from django.shortcuts import render
from .models import Author,Book

# Create your views here.
def books_by_author(request,author_id):
    author=Author.objects.get(id=author_id)
    books=Book.objects.filter(author=author)
    print(author)
    print(books)


    context={
        'author':author,
        'books':books
    }

    return render(request,'book.html',context)