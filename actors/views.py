"""
Este módulo define view classes para gerenciar o modelo Actor, com suporte
para operações de listagem, criação, recuperação, atualização e destruição.
As permissões necessárias são IsAuthenticated e GlobalDefaultPermissions.
"""

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from actors.models import Actor
from actors.serializers import ActorSerializer
from app.permissions import GlobalDefaultPermissions


class ActorCreateListView(generics.ListCreateAPIView):
    """
    View para listar e criar instâncias de Actor.
    Requer autenticação e permissões padrão globais.
    """

    permission_classes = (IsAuthenticated, GlobalDefaultPermissions)
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class ActorRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    View para recuperar, atualizar e destruir instâncias de Actor.
    Requer autenticação e permissões padrão globais.
    """

    permission_classes = (IsAuthenticated, GlobalDefaultPermissions)
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
