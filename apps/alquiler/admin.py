from django.contrib import admin
from .models import Alquiler, Dueno, MetodoPago

@admin.register(Alquiler)
class AlquilerPropiedad(admin.ModelAdmin):
     list_display = ('Usuario','Direccion_Propiedad','Dueno','Inquilino','Fecha_contrato','Precio_mensual','Meses_actualizacion_IPC','Porcentaje_actualizacion','Cancelacion_pago','Observacion','Precio_Pasto')

@admin.register(Dueno)
class AlquilerDueno(admin.ModelAdmin):
     list_display = ('Nombre',)

@admin.register(MetodoPago)
class MetodoPago(admin.ModelAdmin):
     list_display = ('Metodo',)
# Register your models here.
