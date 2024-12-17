"""
Configuração da aplicação 'genres' no Django. Especifica o campo padrão usado
para chaves primárias e o nome da aplicação.
"""

from django.apps import AppConfig


class GenresConfig(AppConfig):
    """Configuração para a aplicação Genres."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "genres"
