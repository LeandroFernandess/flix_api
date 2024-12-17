"""
Este módulo define o serializer para o modelo de Review.

Permite a conversão de instâncias de Review para representações JSON.
"""

from rest_framework import serializers
from reviews.models import Review


class ReviewSerializer(serializers.ModelSerializer):
    """
    Serializer para o modelo Review, permitindo representação completa.

    Este serializer inclui todos os campos do modelo Review.
    """

    class Meta:
        model = Review
        fields = "__all__"
