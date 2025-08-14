from django.db import models

class Author(models.Model): # creates a table
    name = models.CharField(max_length=100) #creates a column named name in the table

#------------------------------------
#Second table
#------------------------------------

class Book(models.Model):
    title = models.CharField(max_length=200)
    publication_year = models.IntegerField()
    author = models.ForeignKey(              #links both tables through id
        Author,
        on_delete=models.CASCADE, # if authour/id is deleted it delets hes/her books
        related_name='books',
    )