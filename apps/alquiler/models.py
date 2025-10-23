from django.db import models


class Alquiler(models.Model):
    Usuario = models.ForeignKey('usuario.Usuario',on_delete=models.CASCADE)
    Direccion_Propiedad = models.CharField()
    Dueno = models.ForeignKey('alquiler.Dueno', on_delete=models.CASCADE, related_name='alquileres')
    Inquilino = models.CharField()
    Fecha_contrato = models.DateField()
    Precio_mensual = models.IntegerField()
    Precio_Agua = models.IntegerField(default=0, blank=True, null=True)
    Precio_ABL = models.IntegerField(default=0, blank=True, null=True)
    Precio_Pasto = models.IntegerField(default=0, blank=True, null=True)
    Meses_actualizacion_IPC = models.IntegerField(blank=True)
    Observacion = models.TextField(blank=True, null=True, max_length=250)
    Cancelacion_pago = models.ForeignKey('alquiler.MetodoPago', on_delete=models.CASCADE, blank=True, null=True)
    Porcentaje_actualizacion = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True, default=0)
    Ultima_actualizacion = models.DateTimeField(auto_now=True)

class Dueno(models.Model):
    Nombre = models.CharField()
    Apellido = models.CharField(blank=True, default='')
    def __str__(self) -> str:
        return self.Nombre
    
class MetodoPago(models.Model):
    Metodo= models.CharField(max_length=20)
    def __str__(self) -> str:
        return self.Metodo

class DatosBancarios(models.Model):
    Dueno = models.OneToOneField('alquiler.Dueno',on_delete=models.CASCADE, related_name='datos_bancarios')
    Alias = models.CharField(blank=True, default='')
    Cbu = models.IntegerField(blank=True, default=0, null=True)
    Titular_cuenta = models.CharField()
    Banco = models.CharField()

    def __str__(self):
        return super().__str__()
