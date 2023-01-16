from django.contrib import admin
from .models import Categoria, Producto

class AdminCategoria(admin.ModelAdmin):
    readonly_fields=('created','updated')

class AdminProducto(admin.ModelAdmin):
    readonly_fields=('created','updated')

admin.site.register(Categoria)
admin.site.register(Producto)
# Register your models here.
