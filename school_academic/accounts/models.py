from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # Add any additional fields you want for your user model
    phone_number = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.username