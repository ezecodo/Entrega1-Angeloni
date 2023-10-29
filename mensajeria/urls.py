from django.urls import path
from . import views


urlpatterns = [
    path('enviar/', views.enviar_mensaje, name='enviar_mensaje'),
    path('ver/', views.ver_mensajes, name='ver_mensajes'),
    path('bandeja_entrada/', views.bandeja_entrada, name='bandeja_entrada'),
    path('mensajes/enviados/', views.mensajes_enviados, name='mensajes_enviados'),
    path('mensajes/eliminar/<int:mensaje_id>/', views.eliminar_mensaje, name='eliminar_mensaje'),

    

]
