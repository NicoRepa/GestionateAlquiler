from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView
from .forms import UsuarioRegisterForm, UsuarioLoginForm
from .models import Usuario
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth import views as auth_views

class RegistroView(CreateView):
    model = Usuario
    form_class = UsuarioRegisterForm
    template_name = 'registration/register.html'
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
    template_name = 'registration/login.html'
    success_url = reverse_lazy('mis_alquileres')
    def dispatch(self, request, *args, **kwargs):
        # Si el usuario ya está autenticado
        if request.user.is_authenticated:
            # Redirecciona a la página de éxito o a donde prefieras
            return redirect(self.success_url)
        # Si no, continua con el flujo normal de la vista
        return super().dispatch(request, *args, **kwargs)


class PasswordResetView(auth_views.PasswordResetView):
    template_name = 'registration/password_reset_form.html'
    email_template_name = 'registration/password_reset_email.html'
    success_url = reverse_lazy('login')
    def form_valid(self, form):
        messages.success(self.request, 'Se ha enviado un correo para restablecer tu contraseña.')
        return super().form_valid(form)

class PasswordResetDoneView(auth_views.PasswordResetDoneView):
    template_name = 'registration/password_reset_done.html'

class PasswordResetConfirmView(auth_views.PasswordResetConfirmView):
    template_name = 'registration/password_reset_confirm.html'
    success_url = reverse_lazy('restablecer-contrasena-complete')

class PasswordResetCompleteView(auth_views.PasswordResetCompleteView):
    template_name = 'registration/password_reset_complete.html'