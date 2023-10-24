
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
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import UserProfile







class UsuarioRegistroView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'usuarios/registro_form.html'
    success_url = reverse_lazy('registro_exitoso')

    def form_valid(self, form):
        response = super().form_valid(form)

       
        profile = UserProfile()
        profile.user = self.object 
        if 'profile_image' in self.request.FILES:
            profile.profile_image = self.request.FILES['profile_image']
        else:
            profile.profile_image = 'img/default_profile.jpg'  
        profile.bio = form.cleaned_data['bio']
        profile.save()

        return response




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




@login_required
def perfil(request):
    profile, created = UserProfile.objects.get_or_create(user=request.user)  

    if request.method == "POST" and 'profile_image' in request.FILES:
        profile.profile_image = request.FILES['profile_image']
        profile.save()
    return render(request, 'usuarios/perfil.html', {'profile': profile})



class RegistroExitosoView(TemplateView):
    template_name = 'usuarios/registro_exitoso.html'
