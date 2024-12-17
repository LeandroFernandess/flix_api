"""
Este módulo define as URLs para as views relacionadas ao modelo Actor.
Inclui rotas para listar, criar, recuperar, atualizar e destruir instâncias de Actor.
"""

from django.urls import path
from . import views

urlpatterns = [
    path("actors/", views.ActorCreateListView.as_view(), name="actor-create-list"),
    path(
        "actors/<int:pk>/",
        views.ActorRetrieveUpdateDestroyView.as_view(),
        name="actor-detail-view",
    ),
]
