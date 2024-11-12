from django.db import models

from admission.models import StudentRegistration
from main_setting.models import Subject
class AbsentReason(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class RecordAttendanceProxy(StudentRegistration):
    class Meta:
        proxy = True
        verbose_name = "Record Attendance"
        verbose_name_plural = "Record Attendance"
        
        
        
from django.db import models

class StudentAssignment(models.Model):
    subject_name = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name="assignments")
    deadline_date = models.DateField()
    remark = models.TextField(blank=True, null=True)
    upload_assignment = models.FileField(upload_to='assignments/', blank=True, null=True)

    def __str__(self):
        return f"{self.subject_name} - {self.deadline_date}"
