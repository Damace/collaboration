from django.contrib.auth.models import AbstractUser
from django.db import models

from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models


class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('Student', 'Student'),
        ('Teacher', 'Teacher'),
        ('Academic', 'Academic'),
        ('Admission', 'Admission'),
        ('Principal', 'Principal'),
        ('Administrator', 'Administrator'),
    ]
    
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

    def __str__(self):
        return self.username

# models.py (continued)

class StudentProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    grade_level = models.CharField(max_length=50)
    # Add more fields specific to students

class TeacherProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    # Add more fields specific to teachers

class AcademicProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    department = models.CharField(max_length=50)
    # Add more fields specific to academics

class AdmissionProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    admission_number = models.CharField(max_length=20)
    # Add more fields specific to admission staff

class PrincipalProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    office_location = models.CharField(max_length=50)
    # Add more fields specific to principals

class AdministratorProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    permissions = models.TextField()  # Use as necessary for admin roles
    # Add more fields specific to administrators
