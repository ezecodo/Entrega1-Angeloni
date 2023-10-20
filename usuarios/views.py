
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from usuarios.forms import CustomUserCreationForm, AuthenticationForm, UsuarioLoginForm
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView
from django.contrib import messages
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator







class UsuarioRegistroView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'usuarios/registro_form.html'
    success_url = reverse_lazy('registro_exitoso')


class RegistroExitosoView(TemplateView):
    template_name = 'usuarios/registro_exitoso.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['login_form'] = UsuarioLoginForm()  
        return context




class CustomLoginView(LoginView):
    form_class = AuthenticationForm
    template_name = 'usuarios/login_form.html' 
    
    def get_success_url(self):
        return reverse_lazy('login_exitoso')
    
    def form_invalid(self, form):
         messages.error(self.request, "Su usuario o contraseña es incorrecta, vuelva a intentarlo de nuevo.")
         return super().form_invalid(form)
    

@method_decorator(login_required, name='dispatch')
class LoginExitosoView(TemplateView):
    template_name = 'usuarios/login_exitoso.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['nombre_de_usuario'] = self.request.user.username
        return context



    
def user_logout(request):
    logout(request)
    return redirect('homepage')