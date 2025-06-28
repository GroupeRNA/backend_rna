from django.contrib.auth.backends import ModelBackend
from app_backend_rna.models.user import User

class CustomUserBackend(ModelBackend):
    def authenticate(self, request, user_name=None, password=None, **kwargs):
        try:
            user = User.objects.get(user_name=user_name)
            if user.check_password(password):
                return user
        except User.DoesNotExist:
            return None
