from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE) # One to Many Relationship
    authors = models.ManyToManyField(Author, related_name = 'books') # Many to Many relationship 

    def __str__(self):
        return self.title


