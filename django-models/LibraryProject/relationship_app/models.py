from django.db import models
from django.contrib.auth.models import User

# Table 1
class Author(models.Model):
    name = models.CharField(max_length=100)

#--------------------------------------------
# Table 2
#--------------------------------------------

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

#--------------------------------------------------
# Table 3
#-----------------------------------------------------

class Library(models.Model):
    name = models.CharField(max_length=100)
    books = models.ManyToManyField(Book)

#--------------------------------------------------
# Table 4
#--------------------------------------------------

class Librarian(models.Model):
    name = models.CharField(max_length=100)
    library = models.OneToOneField(Library, on_delete=models.CASCADE)

#------------------------------------------------------
#Table 5
#-------------------------------------------------------

class UserProfile(models.Model):                

    ROLE_CHOICES = [                            
        ('Admin', 'Admin'),                     
        ('Librarian', 'Librarian'),
        ('Member', 'Member'),
    ]

    user = models.OneToOneField(               
        User,                                   
        on_delete=models.CASCADE                
    )

    role = models.CharField(                   
        max_length=20,                          
        choices=ROLE_CHOICES ,
        default='Member'                   
    )