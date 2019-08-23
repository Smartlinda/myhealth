from health.models import User
from django.contrib.auth.backends import ModelBackend

class EmailBackend(ModelBackend):
    def authenticate(self, email=None, password=None, **kwargs):
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return None
        else:
            if user.check_password(password):
                return user
        return None

    def get_user(self, user_id):
        try:
            user = User.objects.get(id=user_id)
            if user.is_active:
                return user
            return None
        except UserModel.DoesNotExist:
            logging.getLogger("error_logger").error("user with %(user_id)d not found")
            return None
