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
    
    def save_image(self):
        self.save()
    
    def delete_image(self):
        self.delete()
        
    @classmethod
    def get_image_by_id(cls,image_id):
        """
        method to query image from database by Image ID
        """
        image = Image.objects.get(id=image_id)
        return image
    
    @classmethod
    def filter_by_location(cls,location_id):
        img_location = Image.objects.filter(location_id=location_id)
        return img_location

    @classmethod
    def update_image(cls,id,value):
        """
        Method to update image details

        Args:
            id: id of the image being updated
            value:
        """
        cls.objects.filter(pk=id).update(image=value)
        
    @classmethod
    def search_by_name(cls,search_term):
        image = cls.objects.filter(name__icontains=search_term)
        return image


    def __str__(self):
        return self.name
    
# Location Model
class Location(models.Model):
    name = models.CharField(max_length=30)
    
    def save_location(self):
        self.save()
        
    def delete_location(self):
        self.delete()
       
    @classmethod
    def update_location(cls,id,name):
        cls.objects.filter(id=id).update(name=name)
         
    def __str__(self):
        return self.name
# Categories Model
class Category(models.Model):
    name = models.CharField(max_length=30)
    
    def save_category(self):
        self.save()
    
    def delete_category(self):
        self.delete()

    @classmethod
    def update_category(cls,id,name):
        cls.objects.filter(id=id).update(name=name)


    def __str__(self):
        return self.name
