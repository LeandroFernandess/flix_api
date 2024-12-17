"""
Este módulo registra o modelo Review no painel administrativo do Django.

Fornece uma interface para visualizar e gerenciar avaliações de filmes.
"""

from django.contrib import admin
from reviews.models import Review


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    """
    Configura a exibição do modelo Review no admin do Django.

    Define quais campos serão exibidos na lista de avaliações.
    """

    list_display = ("id", "movie", "stars", "comment")
