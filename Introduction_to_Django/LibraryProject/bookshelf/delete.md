To delete a book from the database, I first imported the `Book` model:


from bookshelf.models import Book

book = Book.objects.get(id=3)
book.delete()

