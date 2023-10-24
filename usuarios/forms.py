from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import UserProfile

class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(
        label="Nombre de usuario",
        widget=forms.TextInput(attrs={'class': 'form-control'}),
    )
    email = forms.EmailField(
        label="Correo Electrónico",  
        widget=forms.EmailInput(attrs={'class': 'form-control'}),
    )
    password1 = forms.CharField(
        label="Contraseña",
    )
    password2 = forms.CharField(
        label="Confirmación de contraseña",
    )
    profile_image = forms.ImageField(
        label="Imagen de Perfil", 
        required=False,
        widget=forms.FileInput(attrs={'class': 'form-control'})
    )
    bio = forms.CharField(
        label="Biografía", 
        required=False,
        widget=forms.Textarea(attrs={'class': 'form-control'})
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'profile_image', 'bio']

class UsuarioLoginForm(AuthenticationForm):
    username = forms.CharField(
        label="Nombre de usuario",
    )
    password = forms.CharField(
        label="Contraseña",
        widget=forms.PasswordInput,
    )


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['bio', 'profile_image']
    def __init__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)
        self.fields['profile_image'].widget.attrs.update({'class': 'form-control'})
        self.fields['bio'].widget.attrs.update({'class': 'form-control', 'rows': '5'})