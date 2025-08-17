from django.db import models

class Author(models.Model):  # creates the Author table
    name = models.CharField(max_length=100)  # single column for author name

#------------------------------------------
#second table
#------------------------------------------

class Book(models.Model):
    title = models.CharField(max_length=200)
    publication_year = models.IntegerField()
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,  # if author is deleted, deletes their books
        related_name='books',      
    )