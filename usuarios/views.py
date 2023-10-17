
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from usuarios.forms import CustomUserCreationForm
from django.views.generic import TemplateView




class UsuarioRegistroView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'usuarios/registro_form.html'
    success_url = reverse_lazy('registro_exitoso')


class RegistroExitosoView(TemplateView):
    template_name = 'usuarios/registro_exitoso.html'