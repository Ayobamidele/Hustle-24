# from rest_framework import permissions
# from rest_framework.authentication import (SessionAuthentication,
#                                            TokenAuthentication)
# from rest_framework.permissions import *


# class NotCreateAndIsAdminUser(permissions.IsAdminUser):
#     def has_permission(self, request, view):
#         print(request.user.is_staff, view.action not in ['update', 'partial_update', 'destroy', 'list'])
#         return (view.action not in ['update', 'partial_update', 'destroy', 'list']
#                 and super(NotCreateAndIsAdminUser, self).has_permission(request, view))


# class CreateAndIsAuthenticated(permissions.IsAuthenticated):
#     def has_permission(self, request, view):
#         return (view.action == 'create'
#                 and super(CreateAndIsAuthenticated, self).has_permission(request, view))


# class ViewOnlyAndAllowAny(permissions.AllowAny):
#     def has_permission(self, request, view):
#         print(view.action)
#         return (view.action not in ['update', 'partial_update', 'destroy', 'create']
#                 and super(ViewOnlyAndAllowAny, self).has_permission(request, view))

#     def has_object_permission(self, request, view, obj):
#         return (view.action not in ['update', 'partial_update', 'destroy', 'create']
#                 and super(ViewOnlyAndAllowAny, self).has_permission(request, view))

# class ReadOnly(BasePermission):
#     def has_permission(self, request, view):
#         return request.method in SAFE_METHODS

# class IsOwner(DjangoObjectPermissions):
#     def has_permission(self, request, view):
#         return request.method in SAFE_METHODS

#     def has_object_permission(self, request, view, obj):
#         # print(view.action, obj.shop_set.first().vendor.id, request.user.vendor.id)
#         if request.user.vendor.id == obj.shop_set.first().vendor.id:
#             return True
#             # return view.action in ['update', 'partial_update', 'destroy', 'list', 'create']
