# Register your models here.
from django.contrib import admin

from clientes.models import Cliente


class Clientes(admin.ModelAdmin):
    list_display = ('id', 'nome', 'email','cpf', 'rg', 'celular', 'ativo')
    list_display_links = ('id', 'nome')
    search_fields = ('nome', 'cpf', 'rg',)
    list_filter = ('ativo',)
    list_editable = ('ativo',)
    ordering = ('nome', )
    list_per_page = 25

admin.site.register(Cliente, Clientes)