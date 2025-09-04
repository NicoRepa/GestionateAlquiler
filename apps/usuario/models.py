from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    username = None
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='usuario_set',
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='usuario_permissions',
        blank=True
    )
    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.email}'

# Create your models here.
