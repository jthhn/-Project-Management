from rest_framework import permissions

class IsAdminOrProjectManagerOrReadOnly(permissions.BasePermission):
    """
    Only admins and project managers can create/update/delete tasks.
    Developers can view their assigned tasks.
    """

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.role in ['admin', 'project_manager']
