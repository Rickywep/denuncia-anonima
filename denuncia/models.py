from django.db import models
from django.utils import timezone

# Create your models here.

class Denuncia(models.Model):
    # model fields
    fecha = models.DateTimeField(default=timezone.now)
    nombre_apellido_sospechoso = models.CharField(blank= True, max_length=100)
    apodo_sospechoso = models.CharField(blank= True, max_length=100)
    descripcion = models.TextField(blank= True, max_length=300)
    locacion = models.CharField(blank=True, max_length=255)
    def __str__(self):
        return self.nombre_apellido_sospechoso