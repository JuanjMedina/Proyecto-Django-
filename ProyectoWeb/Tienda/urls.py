from django.urls import path

from .views import Tienda
urlpatterns = [
    path('', Tienda, name="Tienda"),
    
]