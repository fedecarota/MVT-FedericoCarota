from django.db import models
from django.forms import DateTimeField

# Create your models here.
class Persona(models.Model):
    nombre = models.CharField(max_length = 30)
    apellido = models.CharField(max_length = 30)
    edad = models.IntegerField()
    fecha_de_alta = models.DateTimeField(null = True)