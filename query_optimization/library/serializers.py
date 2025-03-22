# library/serializers.py
# from rest_framework import serializers
# from .models import Author, Book

# class AuthorSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Author
#         fields = ['id','name']

# class BookSerializer(serializers.ModelSerializer):
#     authors = serializers.PrimaryKeyRelatedField(queryset=Author.objects.only('id'), many=True)

#     class Meta:
#         model = Book
#         fields = ["id","title","author","authors"]

# query_optimization/library/serializers.py
from rest_framework import serializers
from .models import Author, Book, BookGenre, BookReview, Genre, Publisher
from django.contrib.auth import get_user_model

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['id', 'full_name', 'email']

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name']

class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = ['id', 'name', 'address']

class BookReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookReview
        fields = ['id', 'review_text', 'rating']

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['id', 'name']

class BookSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    publisher = PublisherSerializer()
    reviews = serializers.SerializerMethodField()
    genres = serializers.SerializerMethodField()

    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'publisher', 'published_date', 'reviews', 'genres']

    def get_reviews(self, obj):
        reviews = obj.bookreview_set.all()
        return BookReviewSerializer(reviews, many=True).data

    def get_genres(self, obj):
        genres = [bg.genre for bg in obj.bookgenre_set.all()]
        return GenreSerializer(genres, many=True).data

    def create(self, validated_data):
        publisher_data = validated_data.pop('publisher')
        
        # Get or create publisher
        publisher, _ = Publisher.objects.get_or_create(**publisher_data)
        
        # Create the book instance
        book = Book.objects.create(
            author=self.context['request'].user,
            publisher=publisher,
            **validated_data
        )
        
        return book