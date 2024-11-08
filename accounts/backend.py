from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from django.db.models import Q


UserModel = get_user_model()

def authenticate(self, request, username=None, password=None, **kwargs):
    UserModel = get_user_model()
    user_field = UserModel.USERNAME_FIELD
    if username is None:
        username = kwargs.get(UserModel.USERNAME_FIELD)
    
    try:
        case_insensitive_username_field = '{}__iexact'.format(UserModel.USERNAME_FIELD)
        user = UserModel._default_manager.get(
            Q((f'{user_field}__iexact', username)) | Q(username__iexact=username)
        )
    except UserModel.DoesNotExist:
        UserModel().set_password(password)

    else:
        if user.check_password(password) and self.user_can_authenticate(user):
            return user





class EmailBackend(ModelBackend):
    def authenticate(self, request, **kwargs):
        UserModel = get_user_model()
        try:
            email = kwargs.get('email', None)
            if email is None:
                email = kwargs.get('username', None)
            user = UserModel.objects.get(email=email)
            if user.check_password(kwargs.get('password', None)):
                return user
        except UserModel.DoesNotExist:
            return None
        return None



# class EmailBackend(ModelBackend):
#     def authenticate(self, request, username=None, password=None, **kwargs):
#         try:
#             user = UserModel.objects.get(Q(username__iexact=username) | Q(email__iexact=username))
#         except UserModel.DoesNotExist:
#             UserModel().set_password(password)
#             return
#         except UserModel.MultipleObjectsReturned:
#             user = UserModel.objects.filter(Q(username__iexact=username) | Q(email__iexact=username)).order_by('id').first()

#         if user.check_password(password) and self.user_can_authenticate(user):
#             return user