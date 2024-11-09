from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    # Remove username by setting it to None
    username = None

    # Make email the unique identifier
    email = models.EmailField(unique=True)

    # Set USERNAME_FIELD to email
    USERNAME_FIELD = 'email'
    
    # Required fields for creating a superuser
    REQUIRED_FIELDS = ['first_name', 'last_name']


    def __str__(self):
        return self.email