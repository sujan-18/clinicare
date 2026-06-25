from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsAdminOrOwnProfile(BasePermission):

    def has_permission(self, request, view):
        # Must be logged in for any access
        return request.user and request.user.is_authenticated
    
         # Admin can access any patient record
    def has_object_permission(self, request, view, obj):
        if request.user.is_staff:
            return True
        # Patient can only access their OWN record
        return obj.user == request.user