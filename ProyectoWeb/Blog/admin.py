from django.contrib import admin
from .models import Categoria, Post

class AdminCategoria(admin.ModelAdmin):
    readonly_fields=('created','updated')

class AdminPost(admin.ModelAdmin):
    readonly_fields=('created','updated')
admin.site.register(Categoria,AdminCategoria)
admin.site.register(Post,AdminPost)
# Register your models here.
