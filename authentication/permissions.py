from rest_framework.permissions import BasePermission, SAFE_METHODS

from authentication.models import Role


class IsSupport(BasePermission):
    """Permission to only allow users with Support role get/edit something"""

    def has_permission(self, request, view):
        support_role = Role.objects.get(id=Role.SUPPORT)
        return request.user.role == support_role
