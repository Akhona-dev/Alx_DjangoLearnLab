from rest_framework import serializers
from .models import Author
from .models import Book
from rest_framework.serializers import ValidationError

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__' # allows conversion of columns/fields

    def validate_publication_year(self, value):
        if value > 2025:  
            raise ValidationError("Publication year cannot be in the future!")
        return value

class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['name', 'books'] #specifies which field to convert