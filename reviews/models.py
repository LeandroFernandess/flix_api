"""
Este módulo define o modelo de avaliação para filmes.

Inclui referências a filmes e validações de classificação.
"""

from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from movies.models import Movie


class Review(models.Model):
    """
    Modelo para representar uma avaliação de filme.

    Atributos:
        movie (ForeignKey): Referência ao filme avaliado.
        stars (IntegerField): Classificação em estrelas de 0 a 5.
        comment (TextField): Comentário opcional sobre o filme.
    """

    movie = models.ForeignKey(Movie, on_delete=models.PROTECT, related_name="reviews")
    stars = models.IntegerField(
        validators=[
            MinValueValidator(0, "Avaliação não pode ser inferior a 0 estrelas."),
            MaxValueValidator(5, "Avaliação não pode ser superior a 5 estrelas."),
        ]
    )
    comment = models.TextField(null=True, blank=True)

    def __str__(self):
        """Retorna uma representação em string da avaliação, com o título do filme."""
        return str(self.movie)
