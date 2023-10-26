from django.db import models
from django.contrib.auth.models import User

class Mensaje(models.Model):
    emisor = models.ForeignKey(User, related_name='mensajes_enviados', on_delete=models.CASCADE)
    receptor = models.ForeignKey(User, related_name='mensajes_recibidos', on_delete=models.CASCADE)
    contenido = models.TextField()
    fecha_enviado = models.DateTimeField(auto_now_add=True)
    leido = models.BooleanField(default=False)
    mensaje_original = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL, related_name='respuestas')

    def __str__(self):
        return f"De {self.emisor} a {self.receptor} - {self.fecha_enviado}"

