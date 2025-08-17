from rest_framework import serializers
from .models import Author
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book  # specifies which model to use
        fields = '__all__'  # allows cornversion of all columns/fields

class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)  # nested serializer for related books

    class Meta:
        model = Author
        fields = ['name', 'books']  # includes specific colunns