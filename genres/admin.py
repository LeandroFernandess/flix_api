"""
Registro do modelo 'Genre' na interface administrativa do Django. Define a exibição
dos campos 'id' e 'name' na lista de visualização.
"""

from django.contrib import admin
from genres.models import Genre


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    """Administração do modelo Genre."""

    list_display = ("id", "name")
