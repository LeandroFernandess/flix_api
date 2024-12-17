"""
Configuração de URLs para o projeto Django.

Define os padrões de URL para o projeto, incluindo rotas para o administrador,
bem como endpoints de várias aplicações.
"""

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/", include("authentication.urls")),
    path("api/v1/", include("genres.urls")),
    path("api/v1/", include("actors.urls")),
    path("api/v1/", include("movies.urls")),
    path("api/v1/", include("reviews.urls")),
]
