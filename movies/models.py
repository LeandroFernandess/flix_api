"""
Modelo Movie para representar filmes no Django.

Inclui campos para título, gênero, data de lançamento, atores e resumo.
"""

from django.db import models
from genres.models import Genre
from actors.models import Actor


class Movie(models.Model):

    title = models.CharField(max_length=100)
    genre = models.ForeignKey(Genre, on_delete=models.PROTECT, related_name="movies")
    release_date = models.DateField(null=True, blank=True)
    actors = models.ManyToManyField(Actor, related_name="movies")
    resume = models.TextField(null=True, blank=True)

    def __str__(self):
        # Retorna o título ao representar o filme como string
        return self.title
