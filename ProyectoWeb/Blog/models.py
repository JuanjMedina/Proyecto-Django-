from django.db import models
from django.contrib.auth.models import User
class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name='categoria'
        verbose_name_plural= 'categorias'
    def __str__(self):
        return self.nombre

class Post(models.Model):
    Titulo = models.CharField(max_length=50)
    Contenido = models.CharField(max_length=50)
    Imagen = models.ImageField(upload_to='blog', null=True, blank=True)
    Autor= models.ForeignKey(User, on_delete=models.CASCADE)
    Categorias= models.ManyToManyField(Categoria)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name='post'
        verbose_name_plural= 'posts'
    def __str__(self):
        return self.Titulo
# Create your models here.
