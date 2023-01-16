from django.urls import path
from .views import Servicios
urlpatterns = [
    path('',Servicios, name="Servicios"),
    
] 