"""
Este script serve como utilitário de linha de comando do Django para tarefas administrativas.

Ele define o módulo de configurações padrão para o aplicativo Django
e executa comandos via linha de comando.
"""

import os
import sys


def main():
    """
    Executa tarefas administrativas.

    Define a variável de ambiente para o módulo de configurações do Django e
    chama a interface de linha de comando do Django para executar tarefas.
    """
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Não foi possível importar o Django. Tem certeza de que ele está instalado e "
            "disponível na sua variável de ambiente PYTHONPATH? Você se "
            "lembrou de ativar um ambiente virtual?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
