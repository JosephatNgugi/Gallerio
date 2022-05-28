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
# Location Model
# Categories Model
