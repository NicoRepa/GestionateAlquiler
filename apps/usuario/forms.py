from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from .models import Usuario
from django.core.exceptions import ValidationError


class UsuarioForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ['username','first_name','last_name', 'password1', 'password2']