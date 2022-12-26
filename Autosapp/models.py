from django.db import models

# Create your models here.
class Autos(models.Model):
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    año = models.CharField(max_length=10)
    transmicion = models.CharField(max_length=30)
    kilometraje = models.CharField(max_length=50)
    estado = models.CharField(max_length=50) 
    def __str__(self):
        return self.marca

class Tienda(models.Model):
    direccion = models.CharField(max_length=50)
    nombre = models.CharField(max_length=50)
    tel = models.CharField(max_length=11)
    horario = models.CharField(max_length=30)
    correo = models.CharField(max_length=30)
    calidad = models.CharField(max_length=30)
    def __str__(self):
        return self.nombre


class Repuesto(models.Model):
    motores = models.CharField(max_length=50)
    neumaticos = models.CharField(max_length=50)
    llantas = models.CharField(max_length=50)
    aceites = models.CharField(max_length=50)
    baterias = models.CharField(max_length=50)
    suspensiones = models.CharField(max_length=50)
    autos = models.ForeignKey(Autos,on_delete=models.CASCADE)
    tiendas = models.ForeignKey(Tienda,on_delete=models.CASCADE)
    






