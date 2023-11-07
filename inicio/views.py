from django.shortcuts import render
from libros.models import Libro 

def homepage(request):
    libros_recientes = list(Libro.objects.all()[:10])  
    libros_recientes_grupo = [libros_recientes[i:i+3] for i in range(0, len(libros_recientes), 3)]
    return render(request, 'inicio/homepage.html', {'libros_recientes': libros_recientes_grupo})


def about(request):
    return render(request, 'inicio/about.html')
