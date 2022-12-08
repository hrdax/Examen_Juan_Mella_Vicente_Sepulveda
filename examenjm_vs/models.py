from django.db import models

# Create your models here.
class Cliente(models.Model):
    Rut=models.CharField(max_length=50)
    Nombre=models.CharField(max_length=50)
    Apellido=models.CharField(max_length=50)
    sector=models.CharField(max_length=50)
    estado=models.CharField(max_length=50)