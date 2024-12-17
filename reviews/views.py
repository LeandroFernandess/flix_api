"""
Este módulo define as views para operações de CRUD no modelo Review.

Inclui views para criar, listar, recuperar, atualizar e excluir instâncias de Review, com controle de acesso através de permissões.
"""

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from reviews.models import Review
from reviews.serializers import ReviewSerializer
from app.permissions import GlobalDefaultPermissions


class ReviewCreateListView(generics.ListCreateAPIView):
    """Permite criar e listar reviews."""

    permission_classes = (IsAuthenticated, GlobalDefaultPermissions)
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class ReviewRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """Permite recuperar, atualizar e excluir reviews."""

    permission_classes = (IsAuthenticated, GlobalDefaultPermissions)
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
