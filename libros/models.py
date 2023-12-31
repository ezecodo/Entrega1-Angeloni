from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

class Libro(models.Model):
    titulo = models.CharField(max_length=255)
    autor = models.CharField(max_length=100)
    genero = models.CharField(max_length=50)
    descripcion = RichTextField(blank=True, null=True)
    imagen = models.ImageField(upload_to='libros/', blank=True, null=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='libros', null=True)
    ano_publicacion = models.IntegerField('Año de Publicación', blank=True, null=True)


    def __str__(self):
        return self.titulo
    