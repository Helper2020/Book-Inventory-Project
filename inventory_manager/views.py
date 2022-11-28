from django.shortcuts import render
from .models import Book, Author, SupportTicket, Genre
from django.views import generic
from django.views.generic import ListView, UpdateView

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
    
    return render(request, 'inventory_manager/index.html', context=info)

class BookCatalog(ListView):
    model = Book
    context_object_name = 'book_catalog'
    template_name = 'inventory_manager/bookcatalog.html'

    def get_queryset(self):
        return Book.objects.order_by('title')


class BookInfo(generic.DetailView):
    model = Book
    template_name = 'inventory_manager/bookinfo.html'