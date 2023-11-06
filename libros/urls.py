from django.urls import path
from . import views
from .views import IngresarLibroView, EditarLibroView

urlpatterns = [
    path('ingresar/', IngresarLibroView.as_view(), name='ingresar_libro'),
    path('libro/editar/<int:pk>/', EditarLibroView.as_view(), name='editar_libro'),
    path('lista_libros/', views.lista_libros, name='lista_libros'),
    path('libros/eliminar/<int:libro_id>/', views.eliminar_libro, name='eliminar_libro'),
    path('libros/detalle/', views.lista_detalle_libros, name='lista_detalle_libros'),
    
   
    
]
