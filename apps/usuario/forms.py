from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm, AuthenticationForm
from .models import Usuario
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate

class UsuarioRegisterForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ['email','first_name','last_name', 'password1', 'password2']

class UsuarioLoginForm(AuthenticationForm):
    username = forms.EmailField()
    def clean(self):
        email = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if email and password:
            self.user_cache = authenticate(self.request, username=email, password=password)
            if self.user_cache is None:
                raise forms.ValidationError(
                    self.error_messages['invalid_login'],
                    code='invalid_login',
                    params={'username': self.username_field.verbose_name},
                )
        return self.cleaned_data