from rest_framework.permissions import BasePermission, SAFE_METHODS
from rest_framework.views import View, Request
from rest_framework import permissions


class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request: Request, view: View):
        return request.user.is_superuser or request.method in SAFE_METHODS
