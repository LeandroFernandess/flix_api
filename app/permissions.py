"""
Define permissões padrão globais para o uso em APIs RESTful.

Inclui verificação baseada em permissões de modelo conforme o método HTTP da requisição.
"""

from rest_framework import permissions


class GlobalDefaultPermissions(permissions.BasePermission):
    """Permissão padrão global baseada nas permissões de modelo por método HTTP."""

    def has_permission(self, request, view):
        """
        Verifica se o usuário tem permissão para executar o método HTTP na visualização.

        Args:
            request: Instância da requisição.
            view: Instância da visualização atual.

        Returns:
            bool: True se o usuário possuir permissão, False caso contrário.
        """
        model_permission_codename = self.__get_model_permission_codename(
            method=request.method,
            view=view,
        )

        if not model_permission_codename:
            return False

        return request.user.has_perm(model_permission_codename)

    def __get_model_permission_codename(self, method, view):
        """
        Gera o codename da permissão baseado no modelo e método HTTP.

        Args:
            method: Método HTTP da requisição.
            view: Instância da visualização atual.

        Returns:
            str or None: Codename da permissão, ou None se não for encontrado.
        """
        try:
            model_name = view.queryset.model._meta.model_name
            app_label = view.queryset.model._meta.app_label
            action = self.__get_action_suffix(method)
            return f"{app_label}.{action}_{model_name}"
        except AttributeError:
            return None

    def __get_action_suffix(self, method):
        """
        Mapeia o método HTTP para o sufixo de ação correspondente.

        Args:
            method: Método HTTP da requisição.

        Returns:
            str: Sufixo de ação correspondente ao método.
        """
        method_actions = {
            "GET": "view",
            "POST": "add",
            "PUT": "change",
            "PATCH": "change",
            "DELETE": "delete",
            "OPTIONS": "view",
            "HEAD": "view",
        }
        return method_actions.get(method, "")
