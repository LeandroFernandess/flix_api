"""
Configuração do aplicativo Django para o módulo de autenticação.
A configuração ajusta parâmetros específicos do modelo de autenticação.
"""

from django.apps import AppConfig


class AuthenticationConfig(AppConfig):
    """
    Configurações para o aplicativo de autenticação.

    Atributos:
        default_auto_field: Define o tipo do campo auto-incrementável padrão.
        name: Nome do aplicativo de autenticação.
    """

    default_auto_field = "django.db.models.BigAutoField"
    name = "authentication"
