from django.contrib import admin
from .models import servicio

class AdminServicios(admin.ModelAdmin):
    readonly_fields=('created','updated',)


admin.site.register(servicio,AdminServicios)
# Register your models here.
