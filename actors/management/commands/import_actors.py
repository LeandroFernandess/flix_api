"""
Este módulo define um comando customizado do Django para importar
uma lista de atores de um arquivo CSV para o banco de dados.
"""

import csv
from datetime import datetime
from django.core.management.base import BaseCommand
from actors.models import Actor


class Command(BaseCommand):
    """Comando para importar lista de atores de um arquivo CSV."""

    help = "Comando para importar lista de atores."

    def add_arguments(self, parser):
        """Define os argumentos aceitos pelo comando."""
        parser.add_argument(
            "file_name", type=str, help="Nome do arquivo CSV na raiz do projeto."
        )

    def handle(self, *args, **options):
        """Manipula a lógica de importação dos dados CSV."""
        file_name = options["file_name"]

        with open(file_name, "r", encoding="utf-8-sig") as file:
            reader = csv.DictReader(file)
            for row in reader:
                name = row["name"]
                birthday = datetime.strptime(row["birthday"], "%Y-%m-%d").date()
                nationality = row["nationality"]

                Actor.objects.create(
                    name=name, birthday=birthday, nationality=nationality
                )
