from django.contrib.auth.models import User
from django.db import models


class Publicacion(models.Model):
    TIPOS_ARTE = [
        ("pintura", "Pintura"),
        ("fotografia", "Fotografía"),
        ("dibujo", "Dibujo"),
        ("ilustracion", "Ilustración"),
        ("escultura", "Escultura"),
        ("otro", "Otro"),
    ]

    autor = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="publicaciones"
    )
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    tipo = models.CharField(max_length=30, choices=TIPOS_ARTE)
    fecha_publicacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo


class Imagen(models.Model):
    publicacion = models.ForeignKey(
        Publicacion, on_delete=models.CASCADE, related_name="imagenes"
    )
    imagen = models.ImageField(upload_to="publicaciones/")

    def __str__(self):
        return f"Imagen de {self.publicacion.titulo}"
