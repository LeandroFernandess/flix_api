"""
Define o serializer GenreSerializer para serializar/deserializar
objetos do modelo Genre usando o Django REST Framework.
"""

from rest_framework import serializers
from genres.models import Genre


class GenreSerializer(serializers.ModelSerializer):
    """Serializer para o modelo Genre."""

    class Meta:
        """Metadados para o serializer."""

        model = Genre
        fields = "__all__"
