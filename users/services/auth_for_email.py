from django.contrib.auth.backends import ModelBackend, UserModel
from django.contrib.auth.models import User


class EmailAuthBackend(ModelBackend):

    def authenticate(self, request, username=None, password=None, **kwarqs):
        user_model = UserModel
        try:
            user = user_model.objects.get(email=username)
            if user.check_password(password): 
                return user
            return None
        except (user_model.DoesNotExist, user_model.MultipleObjectsReturned): 
            return None
    
    def get_user(self, user_id):
        user_model = UserModel
        try:
            return user_model.objects.get(pk=user_id)
        except user_model.DoesNotExist:
            return None