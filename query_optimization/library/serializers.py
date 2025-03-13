# library/serializers.py
from rest_framework import serializers
from .models import Author, Book

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id','name']

class BookSerializer(serializers.ModelSerializer):
    authors = serializers.PrimaryKeyRelatedField(queryset=Author.objects.only('id'), many=True)

    class Meta:
        model = Book
        fields = ["id","title","author","authors"]
