from rest_framework.permissions import BasePermission

class IsAuthorOrReadOnly(BasePermission):

    def has_object_permission(self, request, view, obj):

        # Everyone can read
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return True

        # Only author can update/delete
        return obj.author == request.user