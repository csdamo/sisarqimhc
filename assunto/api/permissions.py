from rest_framework import permissions


class IsAdminOrReadOnly(permissions.IsAdminUser):
    
    def has_permission(self, request, view):
        
        if request.method == 'GET':
            return True
        
        stuff_permission = bool(request.user and request.user.is_staff)
        return stuff_permission