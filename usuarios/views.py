
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from usuarios.forms import CustomUserCreationForm, AuthenticationForm
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView
from django.contrib import messages
from django.contrib.auth import logout
from django.shortcuts import redirect







class UsuarioRegistroView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'usuarios/registro_form.html'
    success_url = reverse_lazy('registro_exitoso')


class RegistroExitosoView(TemplateView):
    template_name = 'usuarios/registro_exitoso.html'




class CustomLoginView(LoginView):
    form_class = AuthenticationForm
    template_name = 'usuarios/login_form.html' 
    
    def get_success_url(self):
        return reverse_lazy('login_exitoso')
    
    def form_invalid(self, form):
         messages.error(self.request, "Su usuario o contraseña es incorrecta, vuelva a intentarlo de nuevo.")
         return super().form_invalid(form)
    

class LoginExitosoView(TemplateView):
    template_name = 'usuarios/login_exitoso.html'



    
def user_logout(request):
    logout(request)
    return redirect('homepage')