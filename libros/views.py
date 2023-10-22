
from django.shortcuts import render, redirect, get_object_or_404
from .forms import LibroForm
from django.shortcuts import render
from .models import Libro
from django.contrib.auth.decorators import login_required



    


@login_required
def ingresar_libro(request):
    if request.method == 'POST':
        form = LibroForm(request.POST, request.FILES) 
        if form.is_valid():
            titulo = form.cleaned_data['titulo']
            autor = form.cleaned_data['autor']
            if not Libro.objects.filter(titulo=titulo, autor=autor).exists():
                form.save()
                return redirect('homepage')
            else:
                form.add_error('titulo', 'Este libro ya existe en la biblioteca.')
    else:
        form = LibroForm()
    return render(request, 'libros/ingresar_libro.html', {'form': form})




def lista_libros(request):
    libros = Libro.objects.all().order_by('titulo') 
    return render(request, 'libros/lista_libros.html', {'libros': libros})


def editar_libro(request, libro_id):
    libro = get_object_or_404(Libro, pk=libro_id)

    if request.method == 'POST':
        form = LibroForm(request.POST, request.FILES, instance=libro)
        if form.is_valid():
            form.save()
            return redirect('lista_libros')
    else:
        form = LibroForm(instance=libro)

    return render(request, 'libros/editar_libro.html', {'form': form, 'libro': libro})



def eliminar_libro(request, libro_id):
    libro = get_object_or_404(Libro, id=libro_id)

    if request.method == 'POST':
        libro.delete()
        return redirect('lista_libros')

    return render(request, 'libros/eliminar_libro.html', {'libro': libro})

