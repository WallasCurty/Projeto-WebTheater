from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path
from videos import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('/video', include('views.video')),
    path('/', include('viws.index')),
    
]
