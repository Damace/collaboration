from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
        is_student = models.BooleanField(default=False)
        
        def __str__(self):
         return self.username


from django.db import models

class BulkSMS(models.Model):
    phone_number = models.CharField(max_length=15, help_text="Enter a valid phone number.")
    message = models.TextField(help_text="Enter the SMS content.")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"SMS to {self.phone_number} at {self.created_at.strftime('%Y-%m-%d %H:%M:%S')}"
