from django.contrib import admin
from .models import Alquiler, Dueno, MetodoPago, DatosBancarios
@admin.register(Alquiler)
class AlquilerPropiedad(admin.ModelAdmin):
     list_display = ('Usuario','Direccion_Propiedad','Dueno','Inquilino','Fecha_contrato','Precio_mensual','Meses_actualizacion_IPC','Porcentaje_actualizacion','Cancelacion_pago','Observacion','Precio_Pasto','Ultima_actualizacion')

@admin.register(Dueno)
class AlquilerDueno(admin.ModelAdmin):
     list_display = ('Nombre','Apellido')

@admin.register(MetodoPago)
class MetodoPago(admin.ModelAdmin):
     list_display = ('Metodo',)

@admin.register(DatosBancarios)
class DatosBancarios(admin.ModelAdmin):
     list_display = ('Dueno','Alias','Cbu','Titular_cuenta','Banco')
# Register your models here.
