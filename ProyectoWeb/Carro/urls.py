from django.urls import path

from .views import *
app_name= "Carro"
urlpatterns = [
    path("Agregar/<int:producto_id>/", agregar_carro , name="agregar"),
    path("Eliminar/<int:producto_id>/", eliminar_producto , name="Eliminar"),
    path("Restar/<int:producto_id>/", restar_producto , name="Restar"),
    path("LImpiar/", limpiar_carro , name="Limpiar"),
    
]