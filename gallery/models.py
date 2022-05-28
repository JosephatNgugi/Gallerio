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
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=200)
    upload_date = models.DateTimeField(auto_now_add=True)
    location = models.ForeignKey('Location', on_delete=models.CASCADE)
    
# Location Model
class Location(models.Model):
    location = models.CharField(max_length=30)
# Categories Model
