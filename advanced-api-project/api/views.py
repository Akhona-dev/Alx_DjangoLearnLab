from rest_framework.authentication import TokenAuthentication
from rest_framework import generics, permissions
from rest_framework.exceptions import ValidationError
from .models import Author
from .models import Book
from rest_framework import generics
from . import serializers

#-------------------------------------
#first View
#-------------------------------------

class BookListView(generics.ListAPIView): #creates a class based view
    """this class based view retrieves all rows in the book table"""
    queryset = Book.objects.all()   #takes all rows in book and strores them in queryset
    serializer_class = serializers.BookSerializer # class responsible for data converion 
    filterset_fields = ['author', 'publication_year']  # allows ?author=1 in URL
    permission_classes = [permissions.AllowAny]

#-------------------------------------
#second view
#-------------------------------------

class BookDetailView(generics.RetrieveAPIView): #gets the required book by id
    """this class gets the required book instance/row by its id"""
    queryset  = Book.objects.all()
    serializer_class = serializers.BookSerializer
    permission_classes = [permissions.AllowAny]

#------------------------------------------------
#third view
#------------------------------------------------

class BookCreateView(generics.CreateAPIView):
    """this class view allows for creating a new book/book instance/row"""
    queryset = Book.objects.all()
    serializer_class = serializers.BookSerializer
    permission_classes = [permissions.IsAuthenticated] #only logged in users can create

#-------------------------------------------------
#fourth view
#-------------------------------------------------

class BookUpdateView(generics.UpdateAPIView):
    """this class updates the already existing books/rows"""
    queryset = Book.objects.all()
    serializer_class = serializers.BookSerializer
    permission_classes = [permissions.IsAuthenticated] 

#-------------------------------------------------
#fith view
#-------------------------------------------------

class BookDeleteView(generics.DestroyAPIView):
    """This view deletes a book instance by its ID."""
    queryset = Book.objects.all()
    serializer_class = serializers.BookSerializer
    permission_classes = [permissions.IsAuthenticated]

