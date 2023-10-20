from django.urls import path
from .views import UsuarioRegistroView, RegistroExitosoView, CustomLoginView, LoginExitosoView


urlpatterns = [
    path('registro/', UsuarioRegistroView.as_view(), name='registro'),
    path('registro_exitoso/', RegistroExitosoView.as_view(), name='registro_exitoso'),
  
   path('login/', CustomLoginView.as_view(), name='login'), 
    path('login_exitoso/', LoginExitosoView.as_view(), name='login_exitoso'), 
    
]
