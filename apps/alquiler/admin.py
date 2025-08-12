from django.contrib import admin
from .models import Alquiler, Dueno

@admin.register(Alquiler)
class AlquilerPropiedad(admin.ModelAdmin):
     list_display = ('Direccion_Propiedad','Dueno','Inquilino','Fecha_contrato','Precio_mensual','Meses_actualizacion_IPC','Porcentaje_actualizacion')

@admin.register(Dueno)
class AlquilerDueno(admin.ModelAdmin):
     list_display = ('Nombre',)
# Register your models here.
