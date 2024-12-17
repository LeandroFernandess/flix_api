"""
Este módulo define serializadores para o modelo `Movie`, incluindo validações
de campos e métodos para representação de dados relacionados, como atores e gêneros.
"""

from django.db.models import Avg
from rest_framework import serializers
from movies.models import Movie
from genres.serializers import GenreSerializer
from actors.serializers import ActorSerializer


class MovieModelSerializer(serializers.ModelSerializer):
    """Serializador para validação e representação do modelo Movie."""

    class Meta:
        model = Movie
        fields = "__all__"

    def validate_release_date(self, value):
        """Valida se a data de lançamento não é anterior a 1990."""
        if value.year < 1990:
            raise serializers.ValidationError(
                "A data de lançamento não pode ser anterior a 1990."
            )
        return value

    def validate_resume(self, value):
        """Valida se o resumo não excede 500 caracteres."""
        if len(value) > 500:
            raise serializers.ValidationError(
                "O tamanho do resumo não pode ser superior a 500 caracteres."
            )
        return value


class MovieListDetailSerializer(serializers.ModelSerializer):
    """Serializador para listagem e detalhamento do filme, incluindo atores e gênero."""

    actors = ActorSerializer(many=True)
    genre = GenreSerializer()
    rate = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Movie
        fields = ["id", "title", "genre", "actors", "release_date", "rate", "resume"]

    def get_rate(self, obj):
        """Calcula a média das avaliações."""
        rate = obj.reviews.aggregate(Avg("stars"))["stars__avg"]
        if rate:
            return round(rate, 1)
        return None
