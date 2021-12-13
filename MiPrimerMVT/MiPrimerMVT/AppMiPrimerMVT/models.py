from django.db import models

from Proyecto23850.Proyecto1.Proyecto1.views import apellido

# Create your models here.
class Familiar(models.Model):
    nombre = models.CharField(max_length=40)
    fechaDeNacimiento = models.DateField()
    edad = models.IntegerField()
    