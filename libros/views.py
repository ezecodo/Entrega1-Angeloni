from django.db import models

class Libro(models.Model):
    titulo = models.CharField(max_length=255)
    autor = models.CharField(max_length=100)
    genero = models.CharField(max_length=50)
    descripcion = models.TextField(blank=True, null=True)  # Campo opcional

    def __str__(self):
        return self.titulo