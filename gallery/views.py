import datetime as dt
from django.shortcuts import render
from .models import *

# Create your views here.
def homepage(request):
    date = dt.date.today()
    images = Image.objects.all()
    return render(request, 'galleries/index.html', {"date":date, "images":images})

