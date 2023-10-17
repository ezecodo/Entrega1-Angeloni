from django.contrib.auth.forms import UserCreationForm  # Importa desde aquí
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView


class UsuarioRegistroView(CreateView):
    form_class = UserCreationForm
    template_name = 'usuarios/registro_form.html'
    success_url = reverse_lazy('registro_exitoso')


