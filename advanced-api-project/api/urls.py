from django.urls import path
from . import views

urlpatterns = [
    # List all books
    path('books/', views.BookListView.as_view(), name='book-list'),

    # Retrieve a single book by ID
    path('books/<int:pk>/', views.BookDetailView.as_view(), name='book-detail'),

    # Create a new book
    path('books/create/', views.BookCreateView.as_view(), name='book-create'),

    # Update an existing book
    path('books/update/<int:pk>/', views.BookUpdateView.as_view(), name='book-update'),

    # Delete a book
    path('books/delete/<int:pk>/', views.BookDeleteView.as_view(), name='book-delete'),
]