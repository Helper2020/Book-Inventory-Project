from django.shortcuts import render
from .models import Book, Author, SupportTicket, Genre
from django.views import generic


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

class BookCatalog(generic.ListView):
    model = Book
    paginate_by = 20
    context_object_name = 'book_catalog'
    template_name = 'inventory_manager/bookcatalog.html'

    def get_queryset(self):
        return Book.objects.order_by('title')


class BookInfo(generic.DetailView):
    model = Book
    template_name = 'inventory_manager/bookinfo.html'

class AuthorCatalog(generic.ListView):
    model = Author
    paginate_by = 20
    context_object_name = 'author_catalog'
    template_name = 'inventory_manager/authorcatalog.html'
    
    def get_queryset(self):
        return Author.objects.order_by('last_name')

class AuthorInfo(generic.DetailView):
    model = Author
    template_name = 'inventory_manager/authorinfo.html'

class BasicAuthorResultsView(generic.ListView):
    model = Author
    template_name = 'inventory_manager/basicsearchauthorresults.html'
    
    def get_queryset(self):
        first_name = self.request.GET.get('firstname')
        last_name = self.request.GET.get('lastname')
        object_list = Author.objects.filter(first_name__icontains=first_name, last_name__icontains=last_name)
       
        return object_list

class BasicBookResultsView(generic.ListView):
    model = Book
    template_name = 'inventory_manager/basicsearchbookresults.html'
    
    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Book.objects.filter(title__icontains=query)
        return object_list