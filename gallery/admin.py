from django.contrib import admin
from .models import *

# Register your models here.
class ImageAdmin(admin.ModelAdmin):
    list_display = ('name',)
    
admin.site.register(User)
admin.site.register(Image, ImageAdmin)