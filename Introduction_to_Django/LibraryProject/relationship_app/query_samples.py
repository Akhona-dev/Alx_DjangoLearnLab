from . import models

#first query
books_by_author = models.Book.objects.filter(author__name='author name')

#second query
list_library = models.Library.objects.all()

#third query
#retrieve the librarian for a library
librarian = models.Librarian.objects.get(library__id=1)


