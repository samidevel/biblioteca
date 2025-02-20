from django.db import models
from applications.autor.models import Autor

from .managers import LibroManager, CategoriaManager


class Categoria(models.Model):
    nombre =  models.CharField(max_length=30)
    
    objects = CategoriaManager()

    def __str__(self):
        return str(self.id) +'-'+ self.nombre


class Libro(models.Model):
    categoria = models.ForeignKey(Categoria,on_delete=models.CASCADE, related_name='categoria_libro')
    

    autores = models.ManyToManyField(Autor)
    titulo = models.CharField(
        max_length=50
    )
    fecha = models.DateField('Feha de lanzamiento')
    portada = models.ImageField(upload_to='portada')
    visitas = models.PositiveIntegerField()

    objects = LibroManager()

    def __str__(self):
        return  str(self.id) +'-'+ self.titulo 


