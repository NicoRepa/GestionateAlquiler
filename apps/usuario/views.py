from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView
from .forms import UsuarioRegisterForm, UsuarioLoginForm
from .models import Usuario
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth import views as auth_views
from django.contrib.auth import get_user_model

from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.conf import settings
Usuario = get_user_model()
class RegistroView(CreateView):
    model = Usuario
    form_class = UsuarioRegisterForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(self.success_url)
        return super().dispatch(request, *args, **kwargs)
    
    def form_valid(self, form):
        # Guardar el usuario sin activarlo
        user = form.save(commit=False)
        user.is_active = False
        user.save()

        # Generar token y URL de verificación
        uid = urlsafe_base64_encode(force_bytes(user.pk))
        token = default_token_generator.make_token(user)
        # build_absolute_uri() crea la URL completa
        link = self.request.build_absolute_uri(f"/validar/{uid}/{token}/")

        # Enviar correo de verificación
        subject = 'Activa tu cuenta de usuario'
        html_message = render_to_string('registration/email_verificacion.html', {
            'user': user,
            'link': link,
        })
        send_mail(
            subject,
            '',
            settings.EMAIL_HOST_USER,
            [user.email],
            html_message=html_message,
            fail_silently=False,
        )
        messages.success(self.request, 'Se envió un mail para activar tu cuenta. Por favor, revisa tu mail.')
        return redirect(self.success_url)

class ActivarCuentaView(TemplateView):
    def get_template_names(self):
        try:
            uid = force_str(urlsafe_base64_decode(self.kwargs['uidb64']))
            user = get_user_model().objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, get_user_model().DoesNotExist):
            user = None

        if user is not None and default_token_generator.check_token(user, self.kwargs['token']):
            user.is_active = True
            user.save()
            return ['registration/activacion_exitosa.html']
        else:
            return ['registration/activacion_fallida.html']


class InicioView(LoginView):
    form_class = UsuarioLoginForm
    template_name = 'registration/login.html'
    success_url = reverse_lazy('mis_alquileres')
    redirect_authenticated_user = True
    def get_success_url(self):
        return self.success_url

        

class PasswordResetView(auth_views.PasswordResetView):
    template_name = 'registration/password_reset_form.html'
    email_template_name = 'registration/password_reset_email.html'
    success_url = reverse_lazy('login')
    def form_valid(self, form):
        email = form.cleaned_data.get('email')
        if not Usuario.objects.filter(email=email).exists():
            messages.error(self.request, 'El correo electrónico ingresado no es valido')
            return self.form_invalid(form)
        else:
            messages.success(self.request, 'recibirás por mail un enlace para restablecer tu contraseña.')
            return super().form_valid(form)
    
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(self.success_url)
        return super().dispatch(request, *args, **kwargs)

class PasswordResetConfirmView(auth_views.PasswordResetConfirmView):
    template_name = 'registration/password_reset_confirm.html'
    success_url = reverse_lazy('login')
    def form_valid(self, form):
        messages.success(self.request, 'Se ha cambiado la contraseña correctamente.')
        return super().form_valid(form)
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(self.success_url)
        return super().dispatch(request, *args, **kwargs)

