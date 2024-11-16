from django.db import models

from admission.models import StudentRegistration

# Create your models here.
class StudentProxy(StudentRegistration):
    class Meta:
        proxy = True
        verbose_name = "My details"
        verbose_name_plural = "My details"

