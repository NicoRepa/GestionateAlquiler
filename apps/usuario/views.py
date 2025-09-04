from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView
from .forms import UsuarioRegisterForm, UsuarioLoginForm
from .models import Usuario

class RegistroView(CreateView):
    model = Usuario
    form_class = UsuarioRegisterForm
    template_name = 'register.html'
    success_url = reverse_lazy('mis_alquileres')

class InicioView(LoginView):
    form_class = UsuarioLoginForm
    template_name = 'login.html'
    success_url = reverse_lazy('mis_alquileres')
# Create your views here.
