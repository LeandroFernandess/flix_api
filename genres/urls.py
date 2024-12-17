"""
Define os caminhos de URL para as operações de listagem, criação,
recuperação, atualização e exclusão de objetos do modelo Genre.
"""

from django.urls import path
from . import views

urlpatterns = [
    path(
        "genres/",
        views.GenreCreateListView.as_view(),
        name="genre-create-list",
    ),
    path(
        "genres/<int:pk>/",
        views.GenreRetrieveUpdateDestroyView.as_view(),
        name="genre-detail-view",
    ),
]
