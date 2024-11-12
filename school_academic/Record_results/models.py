# systemUsers/models.py
from django.db import models

from main_setting.models import AcademicYear, Class, Stream, Subject, Term
from exam_setting.models import ExamsCategory, GradeScale
from admission.models import StudentRegistration

class EnterResults(models.Model):
    academic_year = models.ForeignKey(AcademicYear, on_delete=models.CASCADE)
    term = models.ForeignKey(Term, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    exam_category = models.ForeignKey(ExamsCategory, on_delete=models.CASCADE)
    class_name = models.ForeignKey(Class, on_delete=models.CASCADE)  # ForeignKey to Class
    stream = models.ForeignKey(Stream, on_delete=models.CASCADE)  # ForeignKey to Stream
    
    def __str__(self):
        return f'Results for {self.subject} - {self.class_name} - {self.stream} - {self.academic_year}'

class StudentsProxy(StudentRegistration):
    class Meta:
        proxy = True
        verbose_name = "Enter Result"
        verbose_name_plural = "Enter Results"


class StudentsAssasmentsProxy(StudentRegistration):
    class Meta:
        proxy = True
        verbose_name = "Enter Student Assessments"
        verbose_name_plural = "Enter Student Assessments"




class QueResults(models.Model):
    academic_year =models.CharField(max_length=100, editable=False)
    term = models.CharField(max_length=100,editable=False)
    programme = models.CharField(max_length=100,editable=False)
    class_name = models.CharField(max_length=100,editable=False)
    stream = models.CharField(max_length=100,editable=False)
    registration_number = models.CharField(max_length=100,editable=False)
    student_name = models.CharField(max_length=255,editable=False)
    exam_type = models.CharField(max_length=100,editable=False)
    subject = models.CharField(max_length=100,editable=False)  # Assuming Subject is another model
    result = models.FloatField()  # Assuming results can be decimal values 
    result_summary = models.CharField(max_length=200)
    # Assuming GradeScale is another model
    
    class Meta:
        verbose_name = "Que Results"
        verbose_name_plural = "Que Results"

    def __str__(self):
        return f"{self.student_name} - {self.subject} ({self.result})"
