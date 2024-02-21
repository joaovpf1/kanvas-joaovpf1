from rest_framework.permissions import SAFE_METHODS
from rest_framework.views import View, Request
from rest_framework import permissions
from contents.models import Content


class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request: Request, view: View):
        return request.user.is_superuser or request.method in SAFE_METHODS


class StudentPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj: Content):
        return (
            request.method in permissions.SAFE_METHODS
            and request.user in obj.course.students.all()
            or request.user.is_superuser
        )
