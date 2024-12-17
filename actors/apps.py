"""
Este módulo configura o aplicativo Django para o modelo Actors.
Define o tipo de campo automático padrão e o nome do aplicativo.
"""

from django.apps import AppConfig


class ActorsConfig(AppConfig):
    """Configuração do aplicativo para o modelo Actors, definindo campos padrão e nome."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "actors"
