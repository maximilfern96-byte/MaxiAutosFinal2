from django.db import models
from django.contrib.auth.models import User


class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.nombre


class Vehiculo(models.Model):
    titulo = models.CharField(max_length=200)
    marca = models.CharField(max_length=100)
    anio = models.IntegerField()
    tipo = models.CharField(max_length=100)

    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='vehiculos/')
    precio = models.IntegerField()

    def __str__(self):
        return self.titulo


class FotoVehiculo(models.Model):
    vehiculo = models.ForeignKey(
        Vehiculo,
        on_delete=models.CASCADE,
        related_name="fotos"
    )

    imagen = models.ImageField(upload_to="vehiculos/")

    def __str__(self):
        return f"Foto de {self.vehiculo.titulo}"


class Favorito(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.usuario.username} - {self.vehiculo.titulo}"