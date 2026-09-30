from django.db import models
import uuid


def generar_codigo():
    return uuid.uuid4().hex  # "lafjhl-lafghlfa-1237jlk-afhj112hi"


class Post(models.Model):
    #dni = models.CharField(max_length=12, unique=True)
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    contenido = models.TextField()
    publicado = models.BooleanField(default=False)
    fecha_creacion = models.DateField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    tags = models.CharField(max_length=300) # ciencia,cultura,
    codigo = models.CharField(max_length=32, unique=True, default=generar_codigo)
    #comentarios = models.CharField(max_length=100, null=True, default=None) # None
    
    def __str__(self):
        return f"Autor: {self.autor}, {self.titulo}"

    def obtener_lista_de_tags(self):
        return self.tags.split(",") # ["cultura", "ciencia", ...]
