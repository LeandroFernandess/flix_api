"""
Configuração do aplicativo Movies no Django.

Define configurações básicas para o aplicativo, como o nome e o campo padrão para chaves primárias.
"""

from django.apps import AppConfig


class MoviesConfig(AppConfig):
    # Define o campo padrão para chaves primárias
    default_auto_field = "django.db.models.BigAutoField"
    # Define o nome do aplicativo
    name = "movies"
