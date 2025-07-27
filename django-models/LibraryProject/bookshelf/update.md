I updated the title of the book with id=3 from "1984" to "Nineteen Eighty-Four" using the following code:


book = Book.objects.get(id=3)
book.title = 'Nineteen Eighty-Four'
book.save()

#Output

>>>
