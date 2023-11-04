from django.contrib.auth.models import User
from .models import Profile
# for building a custom authentication backend
# now you can login with email or password


class EmailAuthBackend():

    def authenticate(self, request, username=None, password=None, ):
        try:
            user = User.objects.get(email=username)
            if user.check_password(password):
                return user
            return None
        except (User.DoesNotExist, User.MultipleObjectsReturned):
            return None

    def get_user(request, user_id):
        try:
            return User.objects.get(pk=user_id)
        except (User.DoesNotExist):
            return None


# function to create profile for user 
def create_profile(backend, user, *args, **kwargs):
    """
    Create user profile for social authentication
    """
    Profile.objects.get_or_create(user=user)