import datetime as dt
from django.shortcuts import render
from .models import *

# Create your views here.
def homepage(request):
    date = dt.date.today()
    images = Image.objects.all()
    return render(request, 'galleries/index.html', {"date":date, "images":images})

def img_location(request, location_id):
    date = dt.date.today()
    images = Image.filter_by_location(location_id)
    return render(request, 'galleries/locate.html',{"date":date,"image_location":images})