from django.conf import settings
from rest_framework.permissions import BasePermission


class CheckAPIKEYAuth(BasePermission):
    """Permissions based on API KEY authentication."""

    def has_permission(self, request, view):
        api_key_secret = request.headers.get("X-API-KEY")
        return api_key_secret == settings.API_KEY
