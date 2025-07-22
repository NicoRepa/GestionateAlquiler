from django import forms
from apps.alquiler.models import Alquiler, Dueno

class CrearAlquilerForm(forms.ModelForm):
    Fecha_contrato = forms.DateField(input_formats=['%d/%m/%Y','%d-%m-%Y'])
    class Meta:
        model = Alquiler
        fields = ['Direccion_Propiedad','Dueno','Inquilino','Fecha_contrato','Precio_mensual','Meses_actualizacion_IPC']

class CrearDuenoForm(forms.ModelForm):
    class Meta:
        model = Dueno
        fields = ['Nombre']