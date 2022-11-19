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
