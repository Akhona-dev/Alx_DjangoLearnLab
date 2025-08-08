from django.db import models

#-------------------------
#first table
#-------------------------

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)

