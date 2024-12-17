"""
Configuração WSGI para o projeto Django.

Esta configuração expõe a aplicação WSGI para o projeto Django, definida em 'app.settings'.
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app.settings")

application = get_wsgi_application()
