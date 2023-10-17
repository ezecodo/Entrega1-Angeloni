from django.urls import path
from .views import UsuarioRegistroView, RegistroExitosoView

urlpatterns = [
    path('registro/', UsuarioRegistroView.as_view(), name='registro'),
    path('registro_exitoso/', RegistroExitosoView.as_view(), name='registro_exitoso'),
    
]
