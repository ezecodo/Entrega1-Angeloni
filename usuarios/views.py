
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
from .forms import UserProfileForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect
from django.contrib import messages
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User







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

    if request.method == "POST":
        form = UserProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Perfil actualizado con éxito.")
        else:
            messages.error(request, "Hubo un error al actualizar el perfil.")
    else:
        form = UserProfileForm(instance=profile)

    return render(request, 'usuarios/perfil.html', {'profile': profile, 'form': form})


class RegistroExitosoView(TemplateView):
    template_name = 'usuarios/registro_exitoso.html'




@login_required
def configuracion(request):
    if request.method == 'POST':
        password_form = PasswordChangeForm(request.user, request.POST)
        
        if password_form.is_valid():
            user = password_form.save()
            update_session_auth_hash(request, user)  
            messages.success(request, 'Tu contraseña ha sido actualizada con éxito!')
            
         
            new_email = request.POST.get('email')
            if new_email and new_email != request.user.email:
                request.user.email = new_email
                request.user.save()
                messages.success(request, 'Tu email ha sido actualizado con éxito!')
            
            return redirect('perfil')
        else:
            messages.error(request, 'Por favor, corrige los errores.')
    else:
        password_form = PasswordChangeForm(request.user)
    
    return render(request, 'usuarios/perfil.html', {
        'password_form': password_form,
    })




def ver_perfil_usuario(request, user_id):
    profile_user = get_object_or_404(User, id=user_id)
    profile = profile_user.userprofile  
    return render(request, 'usuarios/ver_perfil_usuario.html', {'profile_user': profile_user, 'profile': profile})




