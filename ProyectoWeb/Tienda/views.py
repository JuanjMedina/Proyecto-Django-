from django.shortcuts import render
from .models import Categoria, Producto
# Create your views here.
def Tienda(request):
    productos=Producto.objects.all()
    return render(request,'Tienda/Tienda.html',{'productos':productos})


def Categorias(request):
    Categorias = Categoria.objects.all()
    pass