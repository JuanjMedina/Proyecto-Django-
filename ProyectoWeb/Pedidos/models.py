from django.db import models
from django.contrib.auth import get_user_model
from Tienda.models import Producto
from django.db.models import F,Sum,FloatField
User= get_user_model()

class Pedidos(models.Model):
    User= models.ForeignKey(User,on_delete=models.CASCADE)
    created= models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table="pedidos"
        verbose_name="Pedido"
        verbose_name_plural="Pedidos"
        ordering=["id"]
    def __str__(self):
        return self.id

    @property
    def total(self):
        return self.linepedido_set.aggregate(
            total= Sum(F("preico")*F("Cantidad"), outpout_field=FloatField)
        )["Total"]

class LineaPedido(models.Model):
    User= models.ForeignKey(User,on_delete=models.CASCADE)
    producto= models.ForeignKey(Producto,on_delete=models.CASCADE)
    pedido= models.ForeignKey(Pedidos,on_delete=models.CASCADE)
    Cantidad =models.IntegerField(default=1)
    created= models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'{self.Cantidad} de {self.producto.Nombre}'
        
    class Meta:
        db_table="LineaPedidos"
        verbose_name="LineaPedido"
        verbose_name_plural="LineaPedidos"

# Create your models here.
