from django.contrib.auth.forms import UserCreationForm  # Importa desde aquí
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView

class UsuarioRegistroView(CreateView):
    form_class = UserCreationForm
    template_name = 'registro/registro_form.html'
    success_url = reverse_lazy('registro_exitoso')

class RegistroExitosoView(TemplateView):
    template_name = 'registro/registro_exitoso.html'
