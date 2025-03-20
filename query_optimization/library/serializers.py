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

#query_optimization/library/serializers.py
from rest_framework import serializers
from .models import Author,Book,BookGenre,BookReview,Genre,Publisher

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id','name']

class PublisherSerializer(serializers.ModelSerializer):
    class Meta : 
        model = Publisher
        fields = ['id','name','address']

class BookReviewSerializer(serializers.ModelSerializer):
    class Meta : 
        model = BookReview
        fields = ['id', 'review_text', 'rating']

class GenreSerializer(serializers.ModelSerializer):
    class Meta :
        model = Genre
        fields = ['id','name']

class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()
    publisher = PublisherSerializer()
    reviews = BookReviewSerializer(many=True, read_only=True)  # Correct way to handle related fields
    genres = GenreSerializer(many=True, read_only=True)

    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'publisher', 'published_date', 'reviews', 'genres']

    def create(self, validated_data):
        author_data = validated_data.pop('author')
        publisher_data = validated_data.pop('publisher')
        reviews_data = validated_data.pop('reviews', [])
        genres_data = validated_data.pop('genres', [])

        # Create the author and publisher instances
        author = Author.objects.create(**author_data)
        publisher = Publisher.objects.create(**publisher_data)

        # Create the book instance
        book = Book.objects.create(author=author, publisher=publisher, **validated_data)

        # Create reviews if provided and associate them with the book
        for review_data in reviews_data:
            BookReview.objects.create(book=book, **review_data)

        # Create genres and associate them with the book
        for genre_data in genres_data:
            genre_instance = Genre.objects.get(id=genre_data['id'])
            book.genres.add(genre_instance)

        return book