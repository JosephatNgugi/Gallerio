from django.db import models

# Create your models here.
def set_location_unknown():
    return Location.objects.get_or_create(location='unknown')

# # User Model
# class User(models.Model):
#     first_name = models.CharField(max_length=30)
#     last_name = models.CharField(max_length=30)
#     email = models.EmailField()
    
#     def __str__(self):
#         return self.first_name
# Image Model
class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=30)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=200,blank=True)
    upload_date = models.DateTimeField(auto_now_add=True)
    location = models.ForeignKey('Location', on_delete=models.SET(set_location_unknown))
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    
# Location Model
class Location(models.Model):
    name = models.CharField(max_length=30)
    
    def __str__(self):
        return self.name
# Categories Model
class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name
