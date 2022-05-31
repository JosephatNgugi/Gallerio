import datetime as dt
from django.http import Http404
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

def image(request, id):
    try:
        image = Image.get_image_by_id(id)
    except Image.DoesNotExist:
        raise Http404()
    return render(request, "galleries/img_detail.html", {"image": image})

def search_results(request):

    if "image" in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_images = Image.search_by_name(search_term)
        message = f"{search_term}"

        return render(
            request,
            "galleries/search.html",
            {"message": message, "images": searched_images},
        )

    else:
        message = "You haven't searched for any term"
        return render(request, "galleries/search.html", {"message": message})
