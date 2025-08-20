from django.db import models


class Alquiler(models.Model):
    Direccion_Propiedad = models.CharField()
    Dueno = models.ForeignKey('alquiler.Dueno', on_delete=models.CASCADE)
    Inquilino = models.CharField()
    Fecha_contrato = models.DateField()
    Precio_mensual = models.IntegerField()
    Meses_actualizacion_IPC = models.IntegerField()
    Porcentaje_actualizacion = models.DecimalField(max_digits=4, decimal_places=2)

class Dueno(models.Model):
    Nombre = models.CharField()
    def __str__(self) -> str:
        return self.Nombre