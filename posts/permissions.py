from rest_framework import permissions

class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        # Authenticated users only can see the list view
        if request.user.is_authenticated:
            return True
        else:
            return False
        
    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request
        if request.method in permissions.SAFE_METHODS:
            return True
        # write permissions are only allowed to the author of a post
        return obj.author == request.user