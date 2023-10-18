from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(
        label="Nombre de usuario",
        
        widget=forms.TextInput(attrs={'class': 'form-control'}),
    )
    password1 = forms.CharField(
        label="Contraseña",
       
    )
    password2 = forms.CharField(
        label="Confirmación de contraseña",
        
    )

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


class UsuarioLoginForm(AuthenticationForm):
    username = forms.CharField(
        label="Nombre de usuario",
        
    )
    password = forms.CharField(
        label="Contraseña",
        widget=forms.PasswordInput,
        
    )
