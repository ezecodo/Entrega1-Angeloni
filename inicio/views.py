from django.shortcuts import render
from libros.models import Libro 

def homepage(request):
    libros_recientes = Libro.objects.all()[:10] 
    return render(request, 'inicio/homepage.html', {'libros_recientes': libros_recientes})

def about(request):
    return render(request, 'inicio/about.html')
