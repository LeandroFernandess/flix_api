"""
Este módulo define a migração para criação do modelo Movie.

Inclui campos para título, data de lançamento, resumo e relações
com atores e gênero, assegurando integridade referencial e opções de exclusão.
"""

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    # Indica que esta é a migração inicial
    initial = True

    # Define as migrações das quais esta migração depende
    dependencies = [
        ("actors", "0001_initial"),
        ("genres", "0001_initial"),
    ]

    # Operações a serem executadas pela migração
    operations = [
        migrations.CreateModel(
            name="Movie",
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
                ("title", models.CharField(max_length=100)),
                (
                    "release_date",
                    models.DateField(blank=True, null=True),
                ),  # Data de lançamento
                ("resume", models.TextField(blank=True, null=True)),
                (
                    "actors",
                    models.ManyToManyField(
                        related_name="movies", to="actors.actor"
                    ),  # Relação M:N com atores
                ),
                (
                    "genre",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,  # Protege de exclusão se houver relação
                        related_name="movies",
                        to="genres.genre",  # Relação 1:N com gênero
                    ),
                ),
            ],
        ),
    ]
