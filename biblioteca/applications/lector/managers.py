import datetime

from django.db import models
from django.db.models import Q, Count, Avg

from django.db import models

class PrestamoManager(models.Manager):

    def libro_promedio_edades(self):
        resultado = self.filter(
            libro__id='6'
        ).aggregate(
            promedio_edad=Avg('lector__edad')
        )
        return resultado


    def num_libros_prestados(self):
        resultados = self.values(
            'libro'
        ).annotate(num_prestados=Count('libro'))

        for r in resultados:
            print("---")
            print(r, r['num_prestados'])

        return resultados
    