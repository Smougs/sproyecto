from django.db import models

# Create your models here.

class Prestamo(models.Model):
    """
    Modelo de Prestamo
    """
    nombre = models.CharField(max_length=100, null=True, blank=True)
    apellido = models.CharField(max_length=100, null=True, blank=True)
    telefono = models.CharField(max_length=100, null=True, blank=True)
    direccion = models.CharField(max_length=100, null=True, blank=True)
    libro = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return '{}'.format(self.id)
