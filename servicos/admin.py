from django.contrib import admin
from .models import Cliente, Profissional

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display=('nome','sobrenome','email','foto_perfil','celular','cpf','endereco','estado','cep','cidade')

@admin.register(Profissional)
class ProfissionalAdmin(admin.ModelAdmin):
    list_display=('servico','nome','sobrenome','email','foto_perfil','celular','cpf','endereco','estado','cep','cidade')