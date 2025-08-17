from django.db import models
from django.contrib.auth.models import User

#----------------------------------------------
#first table
#----------------------------------------------

class Post(models.Model): #creates a model/table named post

    """the following are collumns on this table/model"""

    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE, #delete post if user is deleted
                               related_name='posts',
    )