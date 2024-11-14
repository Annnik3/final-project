from rest_framework import serializers
from books.models import Book, Author, Genre


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['first_name', 'last_name']

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['name']

class BookSerializer(serializers.ModelSerializer):
    authors = AuthorSerializer(many=True)
    genre = GenreSerializer()

    class Meta:
        model = Book
        fields = ['id', 'title', 'authors', 'genre', 'publication_date', 'quantity']
