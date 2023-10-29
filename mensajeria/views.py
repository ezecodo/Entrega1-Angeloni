from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import MensajeForm
from .models import Mensaje
from django.contrib.auth.models import User


from django.contrib import messages
from django.urls import reverse




@login_required
def enviar_mensaje(request):
    if request.method == "POST":
        form = MensajeForm(request.POST)
        if form.is_valid():
            mensaje = form.save(commit=False)
            mensaje.emisor = request.user
            mensaje.save()
            messages.success(request, 'Mensaje enviado exitosamente.')
            return redirect(reverse('bandeja_entrada'))  

    else:
        form = MensajeForm()

    return redirect('mensajeria/enviar_mensaje.html')



@login_required
def enviar_mensaje_usuario(request, user_id):
    receptor = get_object_or_404(User, id=user_id)

    if request.method == 'POST':
        contenido = request.POST['mensaje']
        Mensaje.objects.create(emisor=request.user, receptor=receptor, contenido=contenido)
        return redirect('lista_libros')  # Ejemplo: 'ver_perfil_usuario' o la URL que prefieras.

    return redirect('lista_libros')





@login_required
def ver_mensajes(request):
    mensajes = Mensaje.objects.filter(receptor=request.user)
    return render(request, 'mensajeria/ver_mensajes.html', {'mensajes': mensajes})

@login_required
def bandeja_entrada(request):
    mensajes_recibidos = Mensaje.objects.filter(receptor=request.user).order_by('-fecha_enviado')
    form = MensajeForm() 
    return render(request, 'mensajeria/bandeja_entrada.html', {'mensajes': mensajes_recibidos, 'form': form})

def mensajes_enviados(request):
    mensajes = Mensaje.objects.filter(emisor=request.user).order_by('-fecha_enviado')
    return render(request, 'mensajeria/mensajes_enviados.html', {'mensajes': mensajes})


@login_required
def eliminar_mensaje(request, mensaje_id):
    try:
        mensaje = Mensaje.objects.get(id=mensaje_id, receptor=request.user)
        mensaje.delete()
        messages.success(request, 'Mensaje eliminado exitosamente.')
    except Mensaje.DoesNotExist:
        messages.error(request, 'Mensaje no encontrado.')

    return redirect('bandeja_entrada')

