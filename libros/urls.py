from django.urls import path
from . import views

urlpatterns = [
    path('ingresar_libro/', views.ingresar_libro, name='ingresar_libro'),
    path('lista_libros/', views.lista_libros, name='lista_libros'),
   
    
]
