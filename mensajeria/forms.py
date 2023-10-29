from django import forms
from .models import Mensaje

class MensajeForm(forms.ModelForm):
    class Meta:
        model = Mensaje
        fields = ['receptor', 'contenido']


class EnviarMensajeUsuarioForm(forms.ModelForm):
    class Meta:
        model = Mensaje
        fields = ['contenido']
