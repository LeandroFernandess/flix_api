"""
Este módulo define o modelo Actor, que representa os atributos de um ator.
O modelo inclui campos para o nome, data de nascimento e nacionalidade.
"""

from django.db import models

NATIONALITY_CHOICES = (
    ("USA", "Estados Unidos"),
    ("BRA", "Brasil"),
)


class Actor(models.Model):
    """Modelo que representa um ator com nome, data de nascimento e nacionalidade."""

    name = models.CharField(max_length=200)
    birthday = models.DateField(null=True, blank=True)
    nationality = models.CharField(
        max_length=100, choices=NATIONALITY_CHOICES, blank=True, null=True
    )

    def __str__(self):
        """Retorna o nome do ator como representação em string do objeto."""
        return self.name
