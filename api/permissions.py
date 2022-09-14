from rest_framework import permissions


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


