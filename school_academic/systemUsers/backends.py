from django.contrib.auth.backends import ModelBackend
from .models import CustomUser

# accounts/backends.py

class RegistrationNumberBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        print(f"Attempting to authenticate user: {username}")
        try:
            user = CustomUser.objects.get(username=username)
        except CustomUser.DoesNotExist:
            print("User does not exist")
            return None
        if user.check_password(password):
            print("Password is correct")
            return user
        print("Password is incorrect")
        return None