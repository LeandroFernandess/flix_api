"""
Este módulo configura a aplicação Django para o app de avaliações.

Define o comportamento padrão e o nome do aplicativo.
"""

from django.apps import AppConfig


class ReviewsConfig(AppConfig):
    """
    Configurações para o app de avaliações.

    Define o campo padrão para chaves primárias e o nome do app.
    """

    default_auto_field = "django.db.models.BigAutoField"
    name = "reviews"
