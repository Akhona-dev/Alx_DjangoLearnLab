from relationship_app.models import Author, Book, Library, Librarian

try:
    author = Author.objects.get(name="J.K. Rowling")
    books_by_author = Book.objects.filter(author=author)
    print(f"Books by {author.name}:")
    for book in books_by_author:
        print(f"- {book.title}")
except Author.DoesNotExist:
    print("Author not found.")

try:
    library = Library.objects.get(name="Central Library")
    books_in_library = library.books.all()
    print(f"\nBooks in {library.name}:")
    for book in books_in_library:
        print(f"- {book.title}")
except Library.DoesNotExist:
    print("Library not found.")

try:
    library = Library.objects.get(name="Central Library")  
    librarian = Librarian.objects.get(library=library)
    print(f"\nLibrarian for {library.name}: {librarian.name}")
except (Library.DoesNotExist, Librarian.DoesNotExist):
    print("Library or Librarian not found.")