from django.db import models
from admission.models import StudentRegistration
from exam_setting.models import GradeScale


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
        
      
      
  
        
# from django.db import models

# class StudentAssessment(models.Model):
#     academic_year = models.CharField(max_length=20, null=True, blank=True)
#     term = models.CharField(max_length=20, null=True, blank=True)
#     programme = models.CharField(max_length=100, null=True, blank=True)
#     student_class = models.CharField(max_length=50, null=True, blank=True)
#     registration_number = models.CharField(max_length=50, null=True, blank=True)
#     first_name = models.CharField(max_length=50, null=True, blank=True)
#     last_name = models.CharField(max_length=50, null=True, blank=True)
#     assessment = models.CharField(max_length=100, null=True, blank=True)
#     assessment_grade = models.CharField(max_length=2, null=True, blank=True)
#   # Assuming grades are like 'A', 'B', etc.

#     def __str__(self):
#         return f"{self.first_name} {self.last_name} - {self.assessment_grade}"


class StudentAssessment(models.Model):
    academic_year = models.CharField(max_length=20, null=True, blank=True)
    term = models.CharField(max_length=20, null=True, blank=True)
    programme = models.CharField(max_length=100, null=True, blank=True)
    student_class = models.CharField(max_length=50, null=True, blank=True)
    registration_number = models.CharField(max_length=50, null=True, blank=True)
    first_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    assessment = models.CharField(max_length=100, null=True, blank=True)
    assessment_grade = models.ForeignKey(GradeScale, on_delete=models.CASCADE, null=False, blank=False)
    # assessment_grade = models.ForeignKey(GradeScale, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.assessment_grade}"