from django.db import models


class Alquiler(models.Model):
    Direccion_Propiedad = models.CharField()
    Dueno = models.ForeignKey('alquiler.Dueno', on_delete=models.CASCADE)
    Inquilino = models.CharField()
    Fecha_contrato = models.DateField()
    Precio_mensual = models.IntegerField()
    Precio_Agua = models.IntegerField(default=0, blank=True)
    Precio_ABL = models.IntegerField(default=0, blank=True)
    Meses_actualizacion_IPC = models.IntegerField(blank=True)
    Observacion = models.CharField(blank=True)
    Porcentaje_actualizacion = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True, default=0)

class Dueno(models.Model):
    Nombre = models.CharField()
    def __str__(self) -> str:
        return self.Nombre