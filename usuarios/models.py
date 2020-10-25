from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class AuthUser(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        abstract = True

class Categorias(models.Model):
    #activo = models.BooleanField(default=False)
    #inactivo = models.BooleanField(default=False)
    nombre = models.CharField(max_length=50)
    def __str__(self):
        return self.nombre

class Usuarios(AuthUser):
    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    aceptar = models.BooleanField(default=False)
    code = models.CharField(max_length=50)
    categoria = models.ForeignKey(Categorias, on_delete=models.RESTRICT, null=True)
    #categoria = models.ForeignKey(Categorias)
    def __str__(self):
        return self.nombre

class Recover(models.Model):
    code = models.CharField(max_length=50)
    usuario = models.ForeignKey(Usuarios, on_delete=models.RESTRICT, null=True )
    def __str__(self):
        return self.code

class Level(models.Model):
    nombre = models.CharField(max_length=50)
    def __str__(self):
        return self.nombre

class Paises(models.Model):
    nombre = models.CharField(max_length=50)
    def __str__(self):
        return self.nombre

class Sentimental(models.Model):
    nombre = models.CharField(max_length=50)
    def __str__(self):
        return self.nombre

class Profile(AuthUser):
    fech_nac = models.CharField(max_length=50)
    genero = models.CharField(max_length=50)
    pais = models.ForeignKey(Paises, on_delete=models.RESTRICT, null=True )
    imagen = models.CharField(max_length=255)
    titulo = models.CharField(max_length=255)
    bio = models.CharField(max_length=255)
    megusta = models.TextField(null=True)
    no_megusta = models.TextField(null=True)
    direccion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=25)
    #usuario = models.ForeignKey(Usuarios, on_delete=models.RESTRICT, null=True )
    nivel = models.ForeignKey(Level, on_delete=models.RESTRICT, null=True )
    sentimental = models.ForeignKey(Sentimental, on_delete=models.RESTRICT, null=True )

class Album(models.Model):
    titulo = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=255)
    usuario = models.ForeignKey(Usuarios, on_delete=models.RESTRICT, null=True )
    nivel = models.ForeignKey(Level, on_delete=models.RESTRICT, null=True )

class Imagen(models.Model): 
    titulo = models.CharField(max_length=255)
    descripcion = models.CharField(max_length=255)
    usuario = models.ForeignKey(Usuarios, on_delete=models.RESTRICT, null=True )
    nivel = models.ForeignKey(Level, on_delete=models.RESTRICT, null=True )
    album = models.ForeignKey(Album, on_delete=models.RESTRICT, null=True )

class Post(models.Model): 
    titulo = models.CharField(max_length=255)
    descripcion = models.TextField(null=True)
    usuario = models.ForeignKey(Usuarios, on_delete=models.RESTRICT, null=True )
    nivel = models.ForeignKey(Level, on_delete=models.RESTRICT, null=True )
    

