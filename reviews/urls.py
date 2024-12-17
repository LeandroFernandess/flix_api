"""
Este módulo define as rotas de URL para as operações do modelo Review.

Permite criar, listar, recuperar, atualizar e excluir instâncias de Review.
"""

from django.urls import path
from . import views

urlpatterns = [
    path("reviews/", views.ReviewCreateListView.as_view(), name="review-create-list"),
    path(
        "reviews/<int:pk>",
        views.ReviewRetrieveUpdateDestroyView.as_view(),
        name="review-detail-view",
    ),
]
