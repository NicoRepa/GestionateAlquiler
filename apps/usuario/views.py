from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView
from .forms import UsuarioForm
from .models import Usuario

class RegistroView(CreateView):
    model = Usuario
    form_class = UsuarioForm
    template_name = 'formulario_usuario.html'
    success_url = reverse_lazy('mis_alquileres')
# Create your views here.
