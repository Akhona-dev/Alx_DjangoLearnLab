from rest_framework import serializers
from .models import Author
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book #spicifies which table/model to use for conversion
        fields = '__all__'  #allows conversion of data in all columns

#-------------------------------------------------
#Second serializer
#-------------------------------------------------

class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True) #allows the conversion of books too

    class Meta:
        model = Author
        fields = ['name', 'books']  #allows conversion in only two field,name and books