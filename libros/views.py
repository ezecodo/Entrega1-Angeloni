
from django.shortcuts import render, redirect, get_object_or_404
from .forms import LibroForm
from django.shortcuts import render
from .models import Libro
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView




    


class IngresarLibroView(LoginRequiredMixin, CreateView):
    model = Libro
    form_class = LibroForm
    template_name = 'libros/ingresar_libro.html'
    success_url = reverse_lazy('lista_libros')  

    def form_valid(self, form):
       
        form.instance.usuario = self.request.user
       
        titulo = form.cleaned_data['titulo']
        autor = form.cleaned_data['autor']
        if not Libro.objects.filter(titulo=titulo, autor=autor).exists():
            return super().form_valid(form)  
        else:
           
            form.add_error('titulo', 'Este libro ya existe en la biblioteca.')
            return self.form_invalid(form) 

class EditarLibroView(LoginRequiredMixin, UpdateView):
    model = Libro
    form_class = LibroForm
    template_name = 'libros/editar_libro.html'
   
    success_url = reverse_lazy('lista_libros')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['libro'] = self.get_object() 
        return context

    def form_valid(self, form):
        return super().form_valid(form)



def lista_libros(request):
    libros = Libro.objects.all().order_by('titulo') 
    return render(request, 'libros/lista_libros.html', {'libros': libros})






def eliminar_libro(request, libro_id):
    libro = get_object_or_404(Libro, id=libro_id)

    if request.method == 'POST':
        libro.delete()
        return redirect('lista_libros')

    return render(request, 'libros/eliminar_libro.html', {'libro': libro})

