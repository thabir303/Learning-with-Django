# from django.db import models


# class Author(models.Model):
#     name = models.CharField(max_length=200)

#     def __str__(self):
#         return self.name

# class Book(models.Model):
#     title = models.CharField(max_length=100)
#     author = models.ForeignKey(Author, on_delete=models.CASCADE) # One to Many Relationship
#     authors = models.ManyToManyField(Author, related_name = 'books') # Many to Many relationship 

#     def __str__(self):
#         return self.title

#query_optimization/library/models.py
from django.db import models
from django.utils import timezone
from .managers import CustomUserManager
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin

class CustomUser(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

class Author(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Publisher(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=150)

    def __str__(self):
        return self.name

def get_default_publisher():
    try:
        return Publisher.objects.first()  # Will return the first Publisher object
    except Publisher.DoesNotExist:
        return None

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author,on_delete=models.CASCADE)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE, default= get_default_publisher)
    published_date = models.DateField(default=timezone.now)

    def __str__(self):
        return self.title

class BookReview(models.Model):
    book = models.ForeignKey(Book,on_delete=models.CASCADE)
    review_text = models.TextField()
    rating = models.IntegerField()

    def __str__(self):
        return f'Review of {self.book.title}'

class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class BookGenre(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.book.title} - {self.genre.name}'