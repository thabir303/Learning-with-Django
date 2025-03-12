# library/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AuthorViewSet, BookViewSet
from . import views
router = DefaultRouter()
router.register(r'authors', AuthorViewSet)
router.register(r'books', BookViewSet)

urlpatterns = [
    path('optimized-queries/', views.optimized_queries, name='optimized_queries'),
    path('prefetch-optimized/', views.prefetch_optimized_queries, name='prefetch_optimized'),
    path('pagination-example/', views.pagination_example, name='pagination_example'),
    path('bulk-create-books/', views.bulk_create_books, name='bulk_create_books'),
    path('index-optimization/', views.index_optimization_example, name='index_optimization'),
    path('', include(router.urls)),
]
