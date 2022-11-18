from django.db import models
from django.urls import reverse 

# Create your models here.
"""
Genre model: This model represents a particular genres.
"""
class Genre(models.Model):
    # Autofield by django is 'id
    name = models.CharField(max_length=100, help_text='Enter a book genre')

    def get_absolute_url(self):
        return reverse('genre-info', args=[str(self.id)])

    def __str__(self):
        return self.name


