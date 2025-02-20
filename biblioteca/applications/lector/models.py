from django.db import models
from applications.libro.models import Libro


#import managers
from .managers import PrestamoManager

class Lector(models.Model):
    nombres= models.CharField(
        max_length=50
    )
    apellidos = models.CharField(
        max_length=50
    )
    nacionalidad = models.CharField(
        max_length=50
    )
    edad = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.nombres


class Prestamo(models.Model):
    lector = models.ForeignKey(Lector, on_delete=models.CASCADE)
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE, related_name='libro_prestamo')
    fecha_prestamo = models.DateField()
    fecha_devolucion = models.DateField(blank=True, null=True)
    devuelto = models.BooleanField()

    objects = PrestamoManager()
    
    def __str__(self):
        return self.libro.titulo

    

