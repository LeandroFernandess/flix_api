"""
Este módulo define a migração para criar o modelo de 'Genre'. Inclui a criação do 
modelo com campos definidos para id e name.
"""

from django.db import migrations, models


class Migration(migrations.Migration):
    """Migração para criar o modelo Genre."""

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Genre",
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
            ],
        ),
    ]
