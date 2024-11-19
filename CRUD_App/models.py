from django.db import models

class Alumnos(models.Model):
    nombre = models.CharField(max_length=100)
    nota1 = models.FloatField()
    nota2 = models.FloatField()
    nota3 = models.FloatField()
    fecha_ingreso = models.DateField()
    carrera = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre