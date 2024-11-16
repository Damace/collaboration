# models.py
from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    





from django.db import models
from django.utils import timezone

class Subject(models.Model):
    CORE = 'Core'
    SUBSIDIARY = 'Subsidiary'
    
    STATUS_CHOICES = [
        (CORE, 'Core'),
        (SUBSIDIARY, 'Subsidiary'),
    ]
    
    department = models.ForeignKey('Department', on_delete=models.CASCADE, null=False, blank=False)
    subject_code = models.CharField(max_length=100, null=False, blank=False)
    subject_name = models.CharField(max_length=255, null=False, blank=False)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=CORE)  # New field added

    def __str__(self):
        return f"{self.subject_code} - {self.subject_name} ({self.get_status_display()})"


class Programme(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    

from django.db import models
from django.db.models.signals import m2m_changed
from django.dispatch import receiver

class Class(models.Model):
    programme = models.ForeignKey(Programme, on_delete=models.CASCADE)
    class_name = models.CharField(max_length=100)
    no_of_stream = models.PositiveIntegerField(default=0, editable=False)
    assigned_streams = models.ManyToManyField('Stream', related_name='classes', blank=True)
    
    def save(self, *args, **kwargs):
        # Count the assigned streams before saving the instance
        self.no_of_stream = self.assigned_streams.count() if self.pk else 0
        
        # Save the instance
        super(Class, self).save(*args, **kwargs)

    def view_assigned_streams(self):
        return ", ".join([stream.name for stream in self.assigned_streams.all()])

    def __str__(self):
        return self.class_name

@receiver(m2m_changed, sender=Class.assigned_streams.through)
def update_no_of_stream(sender, instance, action, **kwargs):
    if action in ["post_add", "post_remove", "post_clear"]:
        instance.no_of_stream = instance.assigned_streams.count()
        instance.save()

#7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777

class SubjectConfig(models.Model):
    class_name = models.ForeignKey(Class, on_delete=models.CASCADE, related_name='subject_configs')
    assigned_streams = models.ManyToManyField('Stream', related_name='subject_configs', blank=True)
    no_of_assigned_subjects = models.PositiveIntegerField(default=0, editable=False)
    subjects = models.ManyToManyField(Subject, related_name='subject_configs', blank=True)

    def save(self, *args, **kwargs):
        super(SubjectConfig, self).save(*args, **kwargs)
        self.no_of_assigned_subjects = self.subjects.count()
        super(SubjectConfig, self).save(update_fields=['no_of_assigned_subjects'])

    def __str__(self):
        return f"Subject Config for {self.class_name}"

@receiver(m2m_changed, sender=SubjectConfig.subjects.through)
def update_no_of_assigned_subjects(sender, instance, action, **kwargs):
    if action in ["post_add", "post_remove", "post_clear"]:
        instance.no_of_assigned_subjects = instance.subjects.count()
        instance.save(update_fields=['no_of_assigned_subjects'])




#######################################################################

class Term(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
class AcademicYear(models.Model):
    STATUS_CHOICES = [
        ('current', 'Current'),
        ('past', 'Past'),
    ]

    name = models.CharField(max_length=255)
    status = models.CharField(max_length=7, choices=STATUS_CHOICES)

    def __str__(self):
        return f"{self.name} ({self.get_status_display()})"
    
class Assessment(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
from django.db import models

class Stream(models.Model):
    name = models.CharField(max_length=10)


    def __str__(self):
        return self.name
    
# systemUsers/models.py

from django.db import models
from django.conf import settings  # Make sure to import settings
from django.utils import timezone
# from .models import AcademicYear, Term, Subject, Class, TeacherProfile

class Teacher(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=15, unique=True)
    username = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.username})"


class SubjectAllocation(models.Model):
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('inactive', 'Inactive'),
    ]
    
    academic_year = models.ForeignKey(AcademicYear, on_delete=models.CASCADE)
    term = models.ForeignKey(Term, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    class_name = models.ForeignKey(Class, on_delete=models.CASCADE)  # Assuming Class is defined in the same or another app
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)  # Foreign key to TeacherProfile
    phone_number = models.CharField(max_length=15, blank=True, null=True)  # Optional, if needed
    assigned_date = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=8, choices=STATUS_CHOICES, default='active')

    def __str__(self):
        return f'{self.subject.subject_code} - {self.subject.subject_name} assigned to {self.class_name} for {self.academic_year}'

# systemUsers/models.py
from django.db import models
from .models import Programme  # Import Programme model

class ResultsDeadline(models.Model):
    program_name = models.ForeignKey(Programme, on_delete=models.CASCADE)  # ForeignKey to Programme
    deadline_date = models.DateField()  # Date field for deadline

    def __str__(self):
        return f'Deadline for {self.program_name}: {self.deadline_date}'
    

    # systemUsers/models.py
from django.db import models

from django.contrib.auth import get_user_model
from django.utils import timezone

class Publish(models.Model):
    program_name = models.ForeignKey(Programme, on_delete=models.CASCADE)  # ForeignKey to Programme
  
    def __str__(self):
        return f'{self.program_name}'



from django.db import models

class Contact(models.Model):
    phone_number = models.CharField(max_length=15)  # Phone number with max length, adjust as needed
    email = models.EmailField(unique=True)  # Unique email field
    address = models.CharField(max_length=255)  # Address with max length

    def __str__(self):
        return f"{self.email} - {self.phone_number}"



