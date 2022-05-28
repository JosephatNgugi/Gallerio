from email.policy import default
from django.db import models

# Create your models here.

# User Model
class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    
    def __str__(self):
        return self.first_name
# Image Model
class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=200)
    upload_date = models.DateTimeField(auto_now_add=True)
    
# Location Model
# Categories Model
