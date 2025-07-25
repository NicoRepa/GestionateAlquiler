from django.shortcuts import render
from django.views.generic import TemplateView,CreateView,DeleteView,UpdateView,ListView
from apps.alquiler.models import Alquiler, Dueno
from apps.alquiler.forms import CrearAlquilerForm, CrearDuenoForm
from django.urls import reverse_lazy

class AlquilerView(TemplateView):
    model = Alquiler
    template_name = 'mis_alquileres.html'

class CrearAlquilerView(CreateView):
    model = Alquiler
    form_class = CrearAlquilerForm
    template_name = 'crear_alquiler.html'
    success_url = reverse_lazy('mis_alquileres') 

class CrearDuenoView(CreateView):
    model = Dueno
    form_class = CrearDuenoForm
    template_name = 'crear_dueno.html'
    success_url = reverse_lazy('mis_alquileres') 
# Create your views here.
