from django.shortcuts import render
from .models import Book
# Create your views here.
def book_list(request):
    books = Book.objects.select_related('publisher').all()
    return render(request, 'library/book_list.html', {'books':books})

def author_books(request, author_id):
    books = Book.objects.prefetch_related('authors').filter(authors__id=author_id)
    
    return render(request, 'library/author_books.html', {'books':books})

def nested_relationship(request):
    books = Book.objects.select_related('publisher').prefetch_related('authors').all()
    return render(request, 'library/nested_relationship.html', {'books':books})