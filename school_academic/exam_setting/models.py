from django.db import models

from main_setting.models import Programme

# Create your models here.
class GradeScale(models.Model):
    program_name = models.ForeignKey(Programme, on_delete=models.CASCADE)
    grade_name = models.CharField(max_length=255)
    minimum_marks = models.PositiveIntegerField()
    grade_point = models.FloatField()
    remark = models.TextField()
    sequence_order = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.grade_name} - {self.program_name.name}"

class GradeDivision(models.Model):
    program_name = models.ForeignKey(Programme, on_delete=models.CASCADE)
    grade_name = models.CharField(max_length=255)
    division_title = models.CharField(max_length=255)
    minimum_division_point = models.FloatField()
    sequence_order = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.grade_name} - {self.division_title} ({self.program_name.name})"
    
class ExamsCategory(models.Model):
    short_name = models.CharField(max_length=50)
    name = models.CharField(max_length=255)
    mandatory = models.BooleanField()

    def __str__(self):
        return f"{self.short_name} - {self.name}"
    
