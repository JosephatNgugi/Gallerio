from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, re_path
from . import views

urlpatterns=[
    path('', views.homepage, name='home'),
    path('search/', views.search_results, name='search_results'),
    re_path(r'^location/(?P<location_id>[\w-]+)/$',views.img_location,name='locations'),
    re_path(r'^image/(\d+)', views.image,name='image')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)