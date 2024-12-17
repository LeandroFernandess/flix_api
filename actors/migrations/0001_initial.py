"""
Este módulo define uma migração para criar o modelo Actor.
Inclui campos para nome, data de nascimento e nacionalidade.
"""

from django.db import migrations, models


class Migration(migrations.Migration):
    """Criação e configuração inicial da migração para o modelo Actor."""

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Actor",
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
                ("name", models.CharField(max_length=200)),
                ("birthday", models.DateField(blank=True, null=True)),
                (
                    "nationality",
                    models.CharField(
                        blank=True,
                        choices=[("USA", "Estados Unidos"), ("BRA", "Brasil")],
                        max_length=100,
                        null=True,
                    ),
                ),
            ],
        ),
    ]
