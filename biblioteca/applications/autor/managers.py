from django.db import models
from django.db.models import Q

class AutorManager(models.Manager):

    def buscar_autor(self, kword):
        resultado =  self.filter(
            nombre__icontains=kword
        )
        return resultado


    def buscar_autor2(self, kword):
        resultado =  self.filter(
            Q(nombre__icontains=kword) | Q(apellidos__icontains=kword)
        )
        return resultado

    def buscar_autor3(self, kword):
        resultado =  self.filter(
            nombre__icontains=kword
        ).filter(
            Q(edad__icontains=35) | Q(edad__icontains=90)
        )

        return resultado

    def buscar_autor4(self, kword):
        resultado =  self.filter(
            edad__gt =35,
            edad__lt=90
        ).order_by('apellidos')
        return resultado