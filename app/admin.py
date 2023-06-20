from django.contrib import admin

from .models import Proposta


@admin.register(Proposta)
class AdminProposta(admin.ModelAdmin):
    list_display = ['id', 'cpf', 'nome', 'valor', 'status']
