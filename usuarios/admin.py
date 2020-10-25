from django.contrib import admin
from .models import Usuarios
# Register your models here.
class UsuariosAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'email', 'password', 'aceptar',)
    search_fields = ['nombre', 'apellido']
    list_filter = ('aceptar',)

admin.site.register(Usuarios, UsuariosAdmin)