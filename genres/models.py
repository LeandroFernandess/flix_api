"""
Define o modelo Genre para representar diferentes gêneros dentro da aplicação.
Este modelo inclui um campo para o nome do gênero.
"""

from django.db import models


class Genre(models.Model):
    """Modelo para representar um gênero com um nome."""

    name = models.CharField(max_length=200)

    def __str__(self):
        """Retorna uma representação em string do nome do gênero."""
        return self.name
