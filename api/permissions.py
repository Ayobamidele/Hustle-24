from rest_framework import permissions
import rest_framework

class AdminAuthenticationPermission(permissions.BasePermission):
    ADMIN_ONLY_AUTH_CLASSES = [rest_framework.authentication.BasicAuthentication, rest_framework.authentication.SessionAuthentication]

    def has_permission(self, request, view):
        user = request.user
        if user and user.is_authenticated:
            return user.is_superuser or \
                not any(isinstance(request._authenticator, x) for x in self.ADMIN_ONLY_AUTH_CLASSES) 
        return False

class IsNotAuthenticated(permissions.BasePermission):
    """
    Allows access only to non authenticated users.
    """
    def has_permission(self, request, view):
        return not request.user.is_authenticated


class IsOwnerOfShop(permissions.BasePermission):
    def has_permission(self, request, view):
        return True

    def has_object_permission(self, request, view, product):
        if request.user.is_authenticated and request.user.is_vendor:
            return product.get_shop.vendor_id == request.user.vendor.id
        return False


class ReadOnly(permissions.AllowAny):
    def has_permission(self, request, view):
        return (view.action not in ['update', 'post','partial_update', 'destroy', 'list', 'create']
                and super(ReadOnly, self).has_permission(request, view))



class NotCreateAndIsAdminUser(permissions.IsAdminUser):
    def has_permission(self, request, view):
        return (view.action in ['update', 'partial_update', 'destroy', 'list'] 
                and super(NotCreateAndIsAdminUser, self).has_permission(request, view))


