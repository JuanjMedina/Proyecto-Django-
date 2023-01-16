from django.shortcuts import render
from .models import servicio
def Servicios(request):
    servicios_disponibles = servicio.objects.all()
    return render(request, "Servicios/servicio.html",{"servicios":servicios_disponibles})

# Create your views here.
