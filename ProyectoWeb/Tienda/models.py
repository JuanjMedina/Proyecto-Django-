from django.db import models



class Categoria(models.Model):
    Nombre = models.CharField(max_length=50)
    Created= models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"

    def __str__(self):
        return self.Nombre
        
class Producto(models.Model):
    Nombre = models.CharField(max_length=50)
    Precio = models.FloatField()
    Imagen = models.ImageField(upload_to='Tienda', null=True, blank=True)
    Categoria= models.ForeignKey(Categoria, on_delete=models.CASCADE)
    Disponibilidad = models.BooleanField(default=True)
    class Meta:
        verbose_name= 'Producto'
        verbose_name_plural= 'Productos'

    def __str__(self):
        return self.Nombre

# Create your models here.
