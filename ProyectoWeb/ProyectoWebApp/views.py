from django.shortcuts import render,HttpResponse
from Carro.Carro import Carro
from Servicios.models import servicio
def inicio(request):
    carro = Carro(request)
    return render(request, "ProyectoWebApp/Home.html")



