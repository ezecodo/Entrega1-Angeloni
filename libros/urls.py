from django.urls import path
from . import views

urlpatterns = [
    path('ingresar/', views.ingresar_libro, name='ingresar_libro'),
    path('lista/', views.lista_libros, name='lista_libros'),
]
