from django.shortcuts import render
from django.views.generic import TemplateView,CreateView,DeleteView,UpdateView,ListView
from apps.alquiler.models import Alquiler, Dueno
from apps.alquiler.forms import CrearAlquilerForm, CrearDuenoForm
from django.urls import reverse_lazy

class AlquilerView(ListView):
    model = Alquiler
    template_name = 'mis_alquileres.html'
    context_object_name = 'alquileres'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Pasa una instancia vacía del formulario para renderizarla
        context['form'] = CrearAlquilerForm()
        return context

class CrearAlquilerView(CreateView):
    model = Alquiler
    form_class = CrearAlquilerForm
    template_name = 'crear_alquiler.html'
    success_url = reverse_lazy('mis_alquileres') 

class CrearDuenoView(CreateView):
    model = Dueno
    form_class = CrearDuenoForm
    #template_name = 'crear_dueno.html'
    success_url = reverse_lazy('mis_alquileres') 
# Create your views here.
