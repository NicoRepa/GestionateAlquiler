from django.db import models

class IndiceInflacion(models.Model):
    Fecha = models.CharField(blank=False, unique=True)
    Porcentaje = models.FloatField(blank=False)

    def __str__(self):
        return super().__str__()

# Create your models here.
