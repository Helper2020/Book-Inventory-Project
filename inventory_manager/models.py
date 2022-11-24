from django.db import models
from django.urls import reverse 


# Create your models here.
"""
Genre model: This model represents a genre.
"""
class Genre(models.Model):
    # Autofield by django is 'id
    name = models.CharField(max_length=100, help_text='Enter a book genre.')

    def get_absolute_url(self):
        return reverse('genre-info', args=[str(self.id)])

    def __str__(self):
        return self.name

"""
Author model: This model represents an author.
"""
class Author(models.Model):
    first_name = models.CharField(max_length=100, help_text='Enter first name of author.')
    last_name = models.CharField(max_length=100, help_text='Enter last name of author.')

    class Meta:
        ordering = ['last_name', 'first_name']

    def get_absolute_url(self):
        return reverse('Author-info', args=[str(self.id)])

    def __str__(self):
        return f'{self.last_name}, {self.first_name}'

"""
Book model: This model represents an book(Not an instance of a book)
"""
class Book(models.Model):
    title = models.CharField(max_length=3000, help_text='Enter book title')
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)
    synopsis = models.TextField(max_length=3000, help_text='A summary of the book content.')
    isbn = models.CharField('ISBN', max_length=20, unique=True, help_text='13-digit ISBN')
    price = models.DecimalField('Price', max_digits=5, decimal_places=2)
    quantity = models.IntegerField('Quantity', help_text='Enter amount in stock.')
    genre = models.ForeignKey(Genre, help_text='Select Genre', on_delete=models.SET_NULL, null=True)
    book_image = models.ImageField(null=True, upload_to='images/')


    def get_absolute_url(self):
        return reverse('book-info', args=[str(self.id)])

    def __str__(self):
        return self.title

"""
SupportTicket model: support tech tickets 
"""
class SupportTicket(models.Model):
    email = models.EmailField(max_length=100)
    topic = models.CharField(max_length=200)
    message = models.TextField(max_length=500)

    def get_absolute_url(self):
        return reverse('book-info', args=[str(self.id)])

    def __str__(self):
        return self.title

 