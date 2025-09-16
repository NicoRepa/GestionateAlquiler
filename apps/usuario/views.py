from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView
from .forms import UsuarioRegisterForm, UsuarioLoginForm
from .models import Usuario
from django.shortcuts import redirect
class RegistroView(CreateView):
    model = Usuario
    form_class = UsuarioRegisterForm
    template_name = 'register.html'
    success_url = reverse_lazy('mis_alquileres')
    def dispatch(self, request, *args, **kwargs):
        # Si el usuario ya está autenticado
        if request.user.is_authenticated:
            # Redirecciona a la página de éxito o a donde prefieras
            return redirect(self.success_url)
        # Si no, continua con el flujo normal de la vista
        return super().dispatch(request, *args, **kwargs)

class InicioView(LoginView):
    form_class = UsuarioLoginForm
    template_name = 'login.html'
    success_url = reverse_lazy('mis_alquileres')
    def dispatch(self, request, *args, **kwargs):
        # Si el usuario ya está autenticado
        if request.user.is_authenticated:
            # Redirecciona a la página de éxito o a donde prefieras
            return redirect(self.success_url)
        # Si no, continua con el flujo normal de la vista
        return super().dispatch(request, *args, **kwargs)
# Create your views here.
