from rest_framework import permissions

class IsAdminOrProjectManager(permissions.BasePermission):
    """
    Only allow admins and project managers to create/update/delete.
    """

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.role in ['admin', 'project_manager']
