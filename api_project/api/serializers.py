from .models import Book
from rest_framework import serializers

#---------------------------
#first serialiser
#---------------------------

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'