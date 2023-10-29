from django.urls import path
from . import views

urlpatterns = [
    path('ingresar_libro/', views.ingresar_libro, name='ingresar_libro'),
    path('lista_libros/', views.lista_libros, name='lista_libros'),
    path('editar/<int:libro_id>/', views.editar_libro, name='editar_libro'),
    path('libros/eliminar/<int:libro_id>/', views.eliminar_libro, name='eliminar_libro'),
    
   
    
]
