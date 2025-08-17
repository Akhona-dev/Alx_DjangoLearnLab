from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework import generics, permissions, filters
from rest_framework.exceptions import ValidationError
from .models import Author
from .models import Book
from rest_framework import generics
from . import serializers
from django_filters import rest_framework

#-------------------------------------
#first View
#-------------------------------------

class BookListView(generics.ListAPIView): #creates a class based view
    """this class based view retrieves all rows in the book table"""
    queryset = Book.objects.all()   #takes all rows in book and strores them in queryset
    serializer_class = serializers.BookSerializer # class responsible for data converion 
    filterset_fields = ['author', 'publication_year']  # allows ?author=1 in URL
    permission_classes = [IsAuthenticatedOrReadOnly]

    """Adds a search functionality"""
    filter_backends = [filters.SearchFilter ,filters.OrderingFilter]
    search_fields = ['title', 'author','publication_year'] #specifies which fields are available for search

    """Allows users to order their search results by title or publication year"""

    ordering_fields = ['title', 'publication_year']

    """This method/function overrides the get method/function of this class"""
    def get_queryset(self): 
        queryset = Book.objects.all()

        """This line gets the parameters of the current user and will use them as argument"""
        params = self.request.query_params
        """the following lines get each field/column(argument)
           from the parammeters(dictionary)
        """
        title = params.get('title')
        author = params.get('author')
        year = params.get('year')

        """The reason why we did not use elif here is to make it possible
           to filter by all these if statements
        """
        if title:
            queryset = queryset.filter(title__icontains=title)
        if author:
            queryset = queryset.filter(author__id=author)
        if year:
            queryset = queryset.filter(publication_year=year)

        return queryset # returns the query

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

