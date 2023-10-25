from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import MensajeForm
from .models import Mensaje

@login_required
def enviar_mensaje(request):
    if request.method == "POST":
        form = MensajeForm(request.POST)
        if form.is_valid():
            mensaje = form.save(commit=False)
            mensaje.emisor = request.user
            mensaje.save()
            return redirect('ver_mensajes')
    else:
        form = MensajeForm()
    return render(request, 'mensajeria/enviar_mensaje.html', {'form': form})

@login_required
def ver_mensajes(request):
    mensajes = Mensaje.objects.filter(receptor=request.user)
    return render(request, 'mensajeria/ver_mensajes.html', {'mensajes': mensajes})

@login_required
def bandeja_entrada(request):
    mensajes_recibidos = Mensaje.objects.filter(receptor=request.user).order_by('-fecha_enviado')
    form = MensajeForm()  # Añade esta línea para incluir el formulario
    return render(request, 'mensajeria/bandeja_entrada.html', {'mensajes': mensajes_recibidos, 'form': form})

