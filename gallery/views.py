import datetime as dt
from django.shortcuts import render

# Create your views here.
def homepage(request):
    date = dt.date.today()
    return render(request, 'galleries/index.html', {"date":date})