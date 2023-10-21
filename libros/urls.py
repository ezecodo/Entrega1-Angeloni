from django.urls import path
from . import views

urlpatterns = [
    path('ingresar_libro/', views.ingresar_libro, name='ingresar_libro'),
   
    
]
