from django.contrib import admin
from .models import IndiceInflacion

@admin.register(IndiceInflacion)
class IndiceInflacion(admin.ModelAdmin):
    list_display = ('Fecha','Porcentaje')
# Register your models here.
