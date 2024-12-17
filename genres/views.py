"""
Define views genéricas para operações CRUD no modelo Genre,
utilizando permissões específicas para autenticação e
acesso global padrão.
"""

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from genres.models import Genre
from genres.serializers import GenreSerializer
from app.permissions import GlobalDefaultPermissions


class GenreCreateListView(generics.ListCreateAPIView):
    """
    View para listar e criar instâncias de Genre.
    Requer autenticação e permissões globais padrões.
    """

    permission_classes = (IsAuthenticated, GlobalDefaultPermissions)
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class GenreRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    View para recuperar, atualizar e destruir instâncias de Genre.
    Requer autenticação e permissões globais padrões.
    """

    permission_classes = (IsAuthenticated, GlobalDefaultPermissions)
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
