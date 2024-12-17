"""
Este módulo define um serializer para o modelo Actor.
O serializer converte as instâncias de Actor em representações de dados que podem ser facilmente renderizadas em JSON.
"""

from rest_framework import serializers
from actors.models import Actor


class ActorSerializer(serializers.ModelSerializer):
    """Serializer para o modelo Actor, incluindo todos os campos do modelo."""

    class Meta:
        model = Actor
        fields = "__all__"
