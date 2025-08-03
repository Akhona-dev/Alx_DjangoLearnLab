from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.conf import settings

user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

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

#----------------------------------------------------------
#Next Week Task
#----------------------------------------------------------


#Table 1
class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field is required")
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(username, email, password, **extra_fields)
    
#------------------------------------------------------------
#Table 2
#------------------------------------------------------------

class CustomUser(AbstractUser):
    date_of_birth = models.DateField(null=True, blank=True)
    profile_photo = models.ImageField(upload_to='profile_photos/', null=True, blank=True)

    objects = CustomUserManager()

    def __str__(self):
        return self.username
    
from django.conf import settings
