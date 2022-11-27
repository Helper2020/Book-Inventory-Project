from django.shortcuts import render
from .models import Book, Author, SupportTicket, Genre

# Create your views here.

def index(request):
    num_books = Book.objects.all().count()
    num_genres = Genre.objects.all().count()
    num_authors =  Author.objects.all().count()

    info = {
        'num_books': num_books,
        'num_authors': num_authors,
        'num_genres': num_genres
    }
    
    return render(request, 'index.html', context=info)
