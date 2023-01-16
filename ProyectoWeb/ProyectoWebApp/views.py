from django.shortcuts import render,HttpResponse
from Servicios.models import servicio
def inicio(request):
    return render(request, "ProyectoWebApp/Home.html")



