from django.db import models

# Create your models here.
# models.py
from django.db import models

from main_setting.models import AcademicYear, Class, Programme, Stream, Term

class Sponsor(models.Model):
    sponsor_name = models.CharField(max_length=255)
    mobile = models.CharField(max_length=15)
    email = models.EmailField()
    postal_address = models.TextField()
    physical_address = models.TextField()

    def __str__(self):
        return self.sponsor_name
    

# models.py
from django.db import models

class EntryCategory(models.Model):
    entry_category = models.CharField(max_length=255)

    def __str__(self):
        return self.entry_category
    

# systemUsers/models.py
from django.db import models
# from main_setting.models import AcademicYear, Term, Programme, Class, EntryCategory, Sponsor  # Import related models

class StudentRegistration(models.Model):
    # Choices for gender and disability fields
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
    ]
    
    DISABILITY_CHOICES = [
        ('none', 'None'),
        ('skin', 'Skin'),
        ('hearing', 'Hearing'),
        ('vision', 'Vision'),
        ('other', 'Other'),
    ]

    # Personal Particulars
    entry_year = models.ForeignKey(AcademicYear, on_delete=models.CASCADE)
    entry_term = models.ForeignKey(Term, on_delete=models.CASCADE)
    entry_programme = models.ForeignKey(Programme, on_delete=models.CASCADE)
    entry_class = models.ForeignKey(Class, on_delete=models.CASCADE)
    entry_category = models.ForeignKey(EntryCategory, on_delete=models.CASCADE)
    sponsor_name = models.ForeignKey(Sponsor, on_delete=models.CASCADE)
    registration_number = models.CharField(max_length=20, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    other_name = models.CharField(max_length=50, blank=True, null=True)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
    birth_date = models.DateField()
    nationality = models.CharField(max_length=50, default='Tanzania')
    disability = models.CharField(max_length=10, choices=DISABILITY_CHOICES, default='none')

    # Next of Kin 1
    next_of_kin1_name = models.CharField(max_length=100)
    next_of_kin1_mobile_number = models.CharField(max_length=15)
    next_of_kin1_email = models.EmailField(blank=True, null=True)
    next_of_kin1_postal_address = models.CharField(max_length=255, blank=True, null=True)

    # Next of Kin 2
    next_of_kin2_name = models.CharField(max_length=100, blank=True, null=True)
    next_of_kin2_mobile_number = models.CharField(max_length=15, blank=True, null=True)
    next_of_kin2_email = models.EmailField(blank=True, null=True)
    next_of_kin2_postal_address = models.CharField(max_length=255, blank=True, null=True)
    next_of_kin2_profile_picture = models.ImageField(upload_to='kin_pictures/', blank=True, null=True)

    def __str__(self):
        return f'{self.registration_number} - {self.first_name} {self.last_name}'

# systemUsers/models.py
import os
from django.db import models
from django.utils import timezone
from .models import StudentRegistration  # Assuming StudentRegistration already exists

class ImportStudent(models.Model):
    file = models.FileField(upload_to='import_files/')
    uploaded_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'Import File - {os.path.basename(self.file.name)}'

class UpgradeStudent(models.Model):
    academic_year = models.ForeignKey(AcademicYear, on_delete=models.CASCADE)
    term = models.ForeignKey(Term, on_delete=models.CASCADE)
    programme = models.ForeignKey(Programme, on_delete=models.CASCADE)
    student_class = models.ForeignKey(Class, on_delete=models.CASCADE)
    class_stream = models.ForeignKey(Stream, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f"Upgrade {self.student_class} - {self.class_stream} ({self.academic_year})"

