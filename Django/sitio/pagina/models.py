from django.db import models

# Create your models here.
class Mimodelo(models.Model):
    nombre = models.CharField(max_length=50)
    forma = models.CharField(max_length=50)
    relleno = models.BooleanField()
    ingredientes = models.TextField()
    precio = models.FloatField() #IntegerField()
    color = models.CharField(max_length=50, null = True)

tamanios = (
    ('bebe','Bebé'),
    ('joven','Joven'),
    ('adulto','Adulto'),
)

class Gato(models.Model):
    color = models.CharField(max_length=10, null= True)
    tamanio = models.CharField(max_length=7, choices=tamanios, default='Joven')
    raza = models.CharField(max_length=30, null= True)