"""
Este módulo define uma migração para o modelo de avaliação de filmes.

Ele cria o modelo `Review`, que inclui campos para avaliar filmes
com estrelas e adicionar comentários, além de uma chave estrangeira
referente ao modelo `Movie`.
"""

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    """Representa uma migração que cria o modelo Review."""

    initial = True

    dependencies = [
        ("movies", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Review",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "stars",
                    models.IntegerField(
                        validators=[
                            django.core.validators.MinValueValidator(
                                0, "Avaliação não pode ser inferior a 0 estrelas."
                            ),
                            django.core.validators.MaxValueValidator(
                                5, "Avaliação não pode ser superior a 5 estrelas."
                            ),
                        ]
                    ),
                ),
                ("comment", models.TextField(blank=True, null=True)),
                (
                    "movie",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="reviews",
                        to="movies.movie",
                    ),
                ),
            ],
        ),
    ]
