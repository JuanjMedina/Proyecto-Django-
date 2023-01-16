from django.urls import path
from .views import *
urlpatterns = [
    path('',Blog, name="Blog"),
    path('categoria/<categoria_id>', Categorias, name="categoria"),
    
] 