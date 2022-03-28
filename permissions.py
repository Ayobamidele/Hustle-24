from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny


class NotCreateAndIsAdminUser(permissions.IsAdminUser):
    def has_permission(self, request, view):
        return (view.action in ['update', 'partial_update', 'destroy', 'list']
                and super(NotCreateAndIsAdminUser, self).has_permission(request, view))


class CreateAndIsAuthenticated(permissions.IsAuthenticated):
    def has_permission(self, request, view):
        return (view.action == 'create'
                and super(CreateAndIsAuthenticated, self).has_permission(request, view))


class ViewOnlyAndAllowAny(permissions.AllowAny):
    def has_permission(self, request, view):
        return (view.action is not in ['update', 'partial_update', 'destroy', 'create']
                and super(ViewOnlyAndAllowAny, self).has_permission(request, view))

