from django.urls import path
from .views import *
urlpatterns = [
    path('', Contactos, name="Contacto"),
]