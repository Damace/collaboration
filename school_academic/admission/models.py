from django.db import models

# Create your models here.
# models.py
from django.db import models

from main_setting.models import AcademicYear, Class, Programme, Stream, Subject, Term


    

# models.py
from django.db import models

class EntryCategory(models.Model):
    entry_category = models.CharField(max_length=255)

    def __str__(self):
        return self.entry_category
    

# systemUsers/models.py
from django.db import models
# from main_setting.models import AcademicYear, Term, Programme, Class, EntryCategory, Sponsor  # Import related models






from django.db import models

from django.db import models

class SetSponsor(models.Model):
    SPONSOR_CHOICES = [
        ('government', 'Government'),
        ('ngos', 'NGOs'),
    ]
    
    sponsor_name = models.CharField(max_length=50, choices=SPONSOR_CHOICES)

    def __str__(self):
        return self.get_sponsor_name_display()  # This will return the human-readable name

class Sponsor(models.Model):
    sponsor_name = models.ForeignKey(SetSponsor, on_delete=models.CASCADE)
    mobile = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    postal_address = models.TextField(blank=True, null=True)
    physical_address = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.sponsor_name.get_sponsor_name_display()  # Return the display name




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
    stream_name = models.ForeignKey(Stream, on_delete=models.CASCADE, null=True, blank=True) 
    subjects = models.ManyToManyField(Subject, blank=True)  # Add this line for subjects
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
    profile_picture = models.ImageField(upload_to='kin_pictures/', blank=True, null=True)

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

# class UpgradeStudent(models.Model):
#     academic_year = models.ForeignKey(AcademicYear, on_delete=models.CASCADE)
#     term = models.ForeignKey(Term, on_delete=models.CASCADE)
#     programme = models.ForeignKey(Programme, on_delete=models.CASCADE)
#     student_class = models.ForeignKey(Class, on_delete=models.CASCADE)
#     class_stream = models.ForeignKey(Stream, on_delete=models.CASCADE, blank=True, null=True)

#     def __str__(self):
#         return f"Upgrade {self.student_class} - {self.class_stream} ({self.academic_year})"




class StudentRegistrationProxy(StudentRegistration):
    class Meta:
        proxy = True
        verbose_name = "Upgrade Students"
        verbose_name_plural = "Upgrade Students"


class UpgradeStudent(models.Model):
    # Empty model

    class Meta:
        verbose_name = "Upgrade Student"
        verbose_name_plural = "Upgrade Students"

    # Optional: Use `pass` if no other methods or fields are defined
    pass

# class UpgradeStudent(models.Model):
#     GENDER_CHOICES = [
#         ('male', 'Male'),
#         ('female', 'Female'),
#     ]
    
#     DISABILITY_CHOICES = [
#         ('none', 'None'),
#         ('skin', 'Skin'),
#         ('hearing', 'Hearing'),
#         ('vision', 'Vision'),
#         ('other', 'Other'),
#     ]

#     # Personal Particulars
#     entry_year = models.ForeignKey(AcademicYear, on_delete=models.CASCADE)
#     entry_term = models.ForeignKey(Term, on_delete=models.CASCADE)
#     entry_programme = models.ForeignKey(Programme, on_delete=models.CASCADE)
#     entry_class = models.ForeignKey(Class, on_delete=models.CASCADE)
#     entry_category = models.ForeignKey(EntryCategory, on_delete=models.CASCADE)
#     sponsor_name = models.ForeignKey(Sponsor, on_delete=models.CASCADE)
#     registration_number = models.CharField(max_length=20, unique=True)
#     first_name = models.CharField(max_length=50)
#     last_name = models.CharField(max_length=50)
#     other_name = models.CharField(max_length=50, blank=True, null=True)
#     gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
#     birth_date = models.DateField()
#     nationality = models.CharField(max_length=50, default='Tanzania')
#     disability = models.CharField(max_length=10, choices=DISABILITY_CHOICES, default='none')

#     # Next of Kin 1
#     next_of_kin1_name = models.CharField(max_length=100)
#     next_of_kin1_mobile_number = models.CharField(max_length=15)
#     next_of_kin1_email = models.EmailField(blank=True, null=True)
#     next_of_kin1_postal_address = models.CharField(max_length=255, blank=True, null=True)

#     # Next of Kin 2
#     next_of_kin2_name = models.CharField(max_length=100, blank=True, null=True)
#     next_of_kin2_mobile_number = models.CharField(max_length=15, blank=True, null=True)
#     next_of_kin2_email = models.EmailField(blank=True, null=True)
#     next_of_kin2_postal_address = models.CharField(max_length=255, blank=True, null=True)
#     next_of_kin2_profile_picture = models.ImageField(upload_to='kin_pictures/', blank=True, null=True)

#     def __str__(self):
#         return f'{self.registration_number} - {self.first_name} {self.last_name}'



from django.db import models

# class RoomAllocation(models.Model):
#     student_name = models.ForeignKey(StudentRegistration, on_delete=models.CASCADE, related_name="room_allocations")
#     room_name = models.CharField(max_length=100)
#     room_number = models.CharField(max_length=50)

#     def __str__(self):
#         return f"{self.student_name} - Room {self.room_name} ({self.room_number})"




from django.db import models

class SchoolContributions(models.Model):
    student_name = models.ForeignKey(StudentRegistration, on_delete=models.CASCADE, related_name="contributions")
    contribution_for = models.CharField(max_length=100)  # For example, "School fees", "Library fund", etc.
    amount = models.DecimalField(max_digits=10, decimal_places=2)  # Amount contributed

    def __str__(self):
        return f"{self.student_name} - {self.contribution_for} - {self.amount}"


from django.db import models

class SetRoom(models.Model):
    dormitory_name = models.CharField(max_length=100, unique=True)
    capacity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.dormitory_name} - Capacity: {self.capacity}"


from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


class RoomAllocation(models.Model):
    student = models.ForeignKey(StudentRegistration, on_delete=models.CASCADE)
    allocated_dormitory = models.ForeignKey(SetRoom, on_delete=models.CASCADE)
    allocation_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.student} allocated to {self.allocated_dormitory.dormitory_name}"

    def save(self, *args, **kwargs):
        # Check if the dormitory has available capacity
        if self.allocated_dormitory.capacity <= RoomAllocation.objects.filter(allocated_dormitory=self.allocated_dormitory).count():
            raise ValidationError(_("This dormitory is at full capacity. Allocation is not allowed."))

        # Proceed with saving if capacity is available
        super().save(*args, **kwargs)

    def remaining_capacity(self):
        """Helper function to calculate and return the remaining capacity of the allocated dormitory."""
        allocated_count = RoomAllocation.objects.filter(allocated_dormitory=self.allocated_dormitory).count()
        return self.allocated_dormitory.capacity - allocated_count

