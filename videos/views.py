from django.shortcuts import render
from videos.models import Categoria,Video



# Create your views here.
def index(request):
    categoria = Categoria.objects.all()
    return render(request,'index.html',{'categoria':categoria})


def videos(request):
    video = Video.objects.all()
    return render(request, 'videos.html', {'video':video})

