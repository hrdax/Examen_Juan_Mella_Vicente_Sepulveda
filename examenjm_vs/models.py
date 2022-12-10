from django.db import models

# Create your models here.
class Cliente(models.Model):
    Rut=models.CharField(max_length=50)
    Nombre=models.CharField(max_length=50)
    Apellido=models.CharField(max_length=50)
    sector=models.CharField(max_length=50)
    estado=models.CharField(max_length=50)


class Usuario(models.Model):
    Nombre=models.CharField(max_length=50)
    Contrasena=models.CharField(max_length=50)
    Rol = models.IntegerField()

class Cuenta(models.Model):
    Codigo=models.BigIntegerField()
    NombreAS=models.CharField(max_length=50)
    Monto=models.BigIntegerField()
    Token=models.CharField(max_length=1000)

class Historialdepagos(models.Model):
    Codigo=models.BigIntegerField()
    NombreAS=models.CharField(max_length=50)
    Monto=models.BigIntegerField()
    Estado=models.CharField(max_length=50)
    Token=models.CharField(max_length=1000)

