from django.db import models
from django.shortcuts import render, redirect
from django.shortcuts import render, redirect
from .forms import IngresarLibroForm
from django.shortcuts import render
from .models import Libro
from django.contrib.auth.decorators import login_required



    


@login_required
def ingresar_libro(request):
    if request.method == 'POST':
        form = IngresarLibroForm(request.POST)
        if form.is_valid():
            # Verificar si el libro ya existe en la biblioteca
            titulo = form.cleaned_data['titulo']
            autor = form.cleaned_data['autor']
            if not Libro.objects.filter(titulo=titulo, autor=autor).exists():
                form.save()
                return redirect('lista_libros')  # Redirigir a la lista de libros
            else:
                # Mostrar mensaje de error si el libro ya existe
                form.add_error('titulo', 'Este libro ya existe en la biblioteca.')
    else:
        form = IngresarLibroForm()
    return render(request, 'libros/ingresar_libro.html', {'form': form})




def lista_libros(request):
    libros = Libro.objects.all().order_by('titulo')  # Ordenar por título
    return render(request, 'libros/lista_libros.html', {'libros': libros})

