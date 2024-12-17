"""
Este módulo define as visualizações relacionadas aos filmes. Inclui classes
para criação, listagem, detalhamento, atualização, exclusão de filmes e
estatísticas de filmes.
"""

from django.db.models import Count, Avg
from rest_framework import generics, views, response, status
from rest_framework.permissions import IsAuthenticated
from movies.models import Movie
from movies.serializers import MovieModelSerializer, MovieListDetailSerializer
from app.permissions import GlobalDefaultPermissions
from reviews.models import Review


class MovieCreateListView(generics.ListCreateAPIView):
    """View para criar e listar filmes."""

    permission_classes = (IsAuthenticated, GlobalDefaultPermissions)
    queryset = Movie.objects.all()
    serializer_class = MovieModelSerializer

    def get_serializer_class(self):
        """Retorna o serializer apropriado dependendo do método HTTP."""
        if self.request.method == "GET":
            return MovieListDetailSerializer
        return MovieModelSerializer


class MovieRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """View para detalhar, atualizar e excluir filmes."""

    permission_classes = (IsAuthenticated, GlobalDefaultPermissions)
    queryset = Movie.objects.all()

    def get_serializer_class(self):
        """Retorna o serializer apropriado dependendo do método HTTP."""
        if self.request.method == "GET":
            return MovieListDetailSerializer
        return MovieModelSerializer


class MovieStatsView(views.APIView):
    """View para exibir estatísticas dos filmes."""

    permission_classes = (IsAuthenticated, GlobalDefaultPermissions)
    queryset = Movie.objects.all()

    def get(self, request):
        """Retorna as estatísticas dos filmes."""
        total_movies = self.queryset.count()
        movies_by_genre = self.queryset.values("genre__name").annotate(
            count=Count("id")
        )
        total_reviews = Review.objects.count()
        average_stars = Review.objects.aggregate(avg_stars=Avg("stars"))["avg_stars"]

        return response.Response(
            data={
                "total_movies": total_movies,
                "movies_by_genre": movies_by_genre,
                "total_reviews": total_reviews,
                "average_stars": round(average_stars, 1) if average_stars else 0,
            },
            status=status.HTTP_200_OK,
        )
