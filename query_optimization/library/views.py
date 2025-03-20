# from django.shortcuts import render
# from django.http import JsonResponse
# from .models import Book, Author
# from django.core.paginator import Paginator
# from django.db.models import Prefetch
# from .serializers import AuthorSerializer, BookSerializer
# from rest_framework import viewsets


# def optimized_queries(request):
#     # fetch books with select_related for one-to-many relationship (Author)
#     books = Book.objects.select_related('author').all()
#     book_data = [{"title": book.title, "author" : book.author.name} for book in books]
#     return JsonResponse(book_data, safe= False)

# def prefetch_optimized_queries(request):
#     # use prefetch_related for Many-to-Many relationship (Author and Book)
#     books = Book.objects.prefetch_related('authors').all()
#     book_data = []
#     for book in books:
#         authors = [author.name for author in book.authors.all()]
#         book_data.append({"title ": book.title,"authors ": authors})
#     return JsonResponse(book_data, safe=False)

# def pagination_example(request):
#     #Paginate books (10 per page)
#     books = Book.objects.all()
#     paginator = Paginator(books,10)
#     page_number = request.GET.get('page',1)
#     page_obj = paginator.get_page(page_number)

#     book_data = [{'title':book.title,"author":book.author.name} for book in page_obj]
#     return JsonResponse(book_data,safe=False)

# def bulk_create_books(request):
#     # Create multiple books using bulk_create
#     books = [
#         Book(title='Book 1',author = Author.objects.first()),
#         Book(title='Book 2', author=Author.objects.first()),
#         Book(title='Book 3', author=Author.objects.first())
#     ]
#     Book.objects.bulk_create(books)
#     return JsonResponse({'message':"Books created successfully"})

# def index_optimization_example(request):
#     # Adding index optimization
#     books = Book.objects.filter(title__icontains='Django') # index optimization for title
#     book_data = [{'title':book.title,'author':book.author.name} for book in books]
#     return JsonResponse(book_data,safe=False)

# class AuthorViewSet(viewsets.ModelViewSet):
#     queryset = Author.objects.all()
#     serializer_class = AuthorSerializer
#     print(f'Author query: ', queryset.explain())

# class BookViewSet(viewsets.ModelViewSet):
#     queryset = Book.objects.prefetch_related('authors').select_related('author').all()
#     serializer_class = BookSerializer
#     print('Book query: ', queryset.explain())


# library/views.py

from rest_framework import viewsets
from .models import Author, Publisher, Book, BookReview, Genre, BookGenre
from .serializers import AuthorSerializer, PublisherSerializer, BookSerializer, BookReviewSerializer, GenreSerializer

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class PublisherViewSet(viewsets.ModelViewSet):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.select_related('author', 'publisher').prefetch_related('bookgenre_set__genre', 'bookreview_set').all()  # Optimized query
    serializer_class = BookSerializer

class BookReviewViewSet(viewsets.ModelViewSet):
    queryset = BookReview.objects.select_related('book').all()
    serializer_class = BookReviewSerializer

class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
