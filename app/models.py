from django.db import models

# Create your models here.

class animales (models.Model):
    nombre = models.CharField(max_length=200)

    def __str__(self):
        return (self).nombre

class atributos (models.Model):
    animal = models.ForeignKey(animales,on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=200)

    def __str__(self):
        return (self).descripcion

