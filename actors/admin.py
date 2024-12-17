"""
Este módulo registra o modelo Actor no painel administrativo do Django.
Define a exibição padrão para os campos do modelo no admin.
"""

from django.contrib import admin
from actors.models import Actor


@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    """Administração do modelo Actor, configurando campos exibidos no painel administrativo."""

    list_display = ("id", "name", "birthday", "nationality")
