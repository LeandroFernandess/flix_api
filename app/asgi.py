"""
Configuração ASGI para o projeto Django.

Define as configurações do ambiente e fornece a aplicação ASGI padrão.
"""

import os
from django.core.asgi import get_asgi_application

# Configure o módulo de configurações do Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app.settings")

# Instância da aplicação ASGI
application = get_asgi_application()
