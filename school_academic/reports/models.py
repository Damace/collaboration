from django.db import models
from admission.models import StudentRegistration


class AnnualReports(models.Model):
    class Meta:
        verbose_name = "Annual report"
        verbose_name_plural = "Annual report"
          
class TermReports(models.Model):
    class Meta:
        verbose_name = "Term report"
        verbose_name_plural = "Term report"
        
class ClassListReports(models.Model):
    class Meta:
        verbose_name = "Class report"
        verbose_name_plural = "Class report"

class SubjectReports(models.Model):
    class Meta:
        verbose_name = "Subject report"
        verbose_name_plural = "Subject report"

class ProgressReports(StudentRegistration):
    class Meta:
        proxy = True
        verbose_name = "Progress report"
        verbose_name_plural = "Progress report"
        
      
      
  
        
from django.db import models

class StudentAssessment(models.Model):
    academic_year = models.CharField(max_length=20)
    term = models.CharField(max_length=20)
    programme = models.CharField(max_length=100)
    student_class = models.CharField(max_length=50)  # Avoid using 'class' as it's a reserved keyword
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    assessment = models.CharField(max_length=100)
    assessment_grade = models.CharField(max_length=2)  # Assuming grades are like 'A', 'B', etc.

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.assessment_grade}"
