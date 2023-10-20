
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from usuarios.forms import CustomUserCreationForm, AuthenticationForm
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView




class UsuarioRegistroView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'usuarios/registro_form.html'
    success_url = reverse_lazy('registro_exitoso')


class RegistroExitosoView(TemplateView):
    template_name = 'usuarios/registro_exitoso.html'


from django.contrib.auth.views import LoginView

class CustomLoginView(LoginView):
    form_class = AuthenticationForm
    template_name = 'usuarios/login_form.html' 

class LoginExitosoView(TemplateView):
    template_name = 'usuarios/login_exitoso.html' 
