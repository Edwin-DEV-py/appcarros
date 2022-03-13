from distutils.command.upload import upload
from django.db import models
from django.forms import CharField

class Usuario(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField(max_length=100)
    fecha = models.DateTimeField(auto_now=False)
    foto = models.ImageField(upload_to ="fotografias")
    cedula = models.CharField(max_length=10)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=10)
    certificado = models.ImageField(upload_to="certificados",null=True)
    
    def __str__(self):
        return self.nombre
    