from datetime import datetime
from django.db import models
from django.forms import DateField, EmailField
from django.contrib.auth.models import User

# Create your models here.
class Corredor (models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    modalidad = models.CharField(max_length=10)
    email = models.EmailField()
    team = models.CharField(max_length=10)
    def __str__ (self):
        return f"Nombre:{self.nombre} - Apellido:{self.apellido} - Modalidad:{self.modalidad} - Email:{self.email} - Team:{self.team}"


class Carreras (models.Model):
    nombre = models.CharField(max_length=20)
    modalidad = models.CharField(max_length=10)
    distancia= models.IntegerField()
    fecha = models.DateField()
    def __str__ (self):
        return f"Nombre:{self.nombre} - Modalidad:{self.modalidad} - Distancia:{self.distancia} - Fecha:{self.fecha}"

class Teams (models.Model):
    nombre = models.CharField(max_length=20)
    modalidad = models.CharField(max_length=10)
    email = models.EmailField()
    def __str__ (self):
        return f"Nombre:{self.nombre} - Modalidad:{self.modalidad} - Email:{self.email}"
# Create your models here.
class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares' , null=True , blank=True)

opciones_consultas = [
    [0, "consulta"], 
    [1, "reclamo"],
    [2, "sugerencia"]
]
class Contacto(models.Model):
    nombre = models.CharField(max_length=50)
    correo = models.EmailField()
    tipo_consulta = models.IntegerField(choices=opciones_consultas)
    mensaje = models.TextField()
    

    def __str__(self): 
        return self.nombre

class Post(models.Model):
    nombre = models.CharField(max_length=50)
    mensaje = models.TextField()
   




