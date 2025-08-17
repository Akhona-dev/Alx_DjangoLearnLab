from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.contrib.auth.models import User
from .models import Book, Author

class BookAPITestCase(APITestCase):

    def setUp(self):
        """Set up test data before each test."""
        self.client = APIClient()

        # Create a user for authenticated endpoints
        self.user = User.objects.create_user(username="testuser", password="password123")
        self.client.login(username="testuser", password="password123")

        # Create an author
        self.author = Author.objects.create(name="Test Author")

        # Create a book
        self.book = Book.objects.create(
            title="Test Book",
            author=self.author,
            publication_year=2022
        )

    def test_list_books(self):
        """Test GET /books/ returns list of books"""
        url = reverse('book-list')
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("Test Book", str(response.data))

    def test_retrieve_book(self):
        """Test GET /books/<id>/ returns a single book"""
        url = reverse('book-detail', args=[self.book.id])
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], "Test Book")

    def test_create_book(self):
        """Test POST /books/create/ creates a book"""
        url = reverse('book-create')
        data = {
            "title": "New Book",
            "author": self.author.id,
            "publication_year": 2023
        }
        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)

    def test_update_book(self):
        """Test PUT /books/update/<id>/ updates a book"""
        url = reverse('book-update', args=[self.book.id])
        data = {
            "title": "Updated Book",
            "author": self.author.id,
            "publication_year": 2025
        }
        response = self.client.put(url, data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, "Updated Book")

    def test_delete_book(self):
        """Test DELETE /books/delete/<id>/ deletes a book"""
        url = reverse('book-delete', args=[self.book.id])
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)