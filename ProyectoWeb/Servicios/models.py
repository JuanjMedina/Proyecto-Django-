from django.db import models

# Create your models here.
class servicio(models.Model):
    titulo=  models.CharField(max_length=50)
    contenido= models.CharField(max_length=50)
    imagen= models.ImageField(upload_to='servicios')
    created = models.DateTimeField(auto_now_add=True)
    updated= models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name='servicio'
        verbose_name_plural= 'servicio'
    def __str__(self):
        return self.titulo