from django.urls import path
from .views import UsuarioRegistroView, RegistroExitosoView, CustomLoginView, LoginExitosoView
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('registro/', UsuarioRegistroView.as_view(), name='registro'),
    path('registro_exitoso/', RegistroExitosoView.as_view(), name='registro_exitoso'),
  
   path('login/', CustomLoginView.as_view(), name='login'), 
   path('login_exitoso/', LoginExitosoView.as_view(), name='login_exitoso'), 
   path('salir/', views.user_logout, name='logout'),
   path('perfil/', views.perfil, name='perfil'),
   path('perfil/<int:user_id>/', views.ver_perfil_usuario, name='ver_perfil_usuario'),
   path('configuracion/', views.configuracion, name='configuracion'),
    
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)