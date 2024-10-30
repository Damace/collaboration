# systemUsers/signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import CustomUser
# Import profile models if you have them

@receiver(post_save, sender=CustomUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        # Add logic to create the respective profile based on role
        pass  # Implement profile creation logic here

@receiver(post_save, sender=CustomUser)
def save_user_profile(sender, instance, **kwargs):
    # Logic to save user profiles
    pass  # Implement profile saving logic here
