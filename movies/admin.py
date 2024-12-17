"""
Configuração do modelo Movie para o Django admin.

Define como os filmes são exibidos na interface administrativa,
incluindo opções para exibir campos essenciais na lista.
"""

from django.contrib import admin
from movies.models import Movie


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    # Define os campos a serem exibidos na lista de filmes
    list_display = ("id", "title", "genre", "release_date", "resume")
