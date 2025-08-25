from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario

@admin.register(Usuario)
class IndiceInflacion(UserAdmin):
    list_display = ('username','first_name','last_name')
# Register your models here.
