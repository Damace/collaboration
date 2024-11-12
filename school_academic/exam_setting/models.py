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
    

class SetExam(models.Model):
    exam_category = models.ForeignKey(ExamsCategory, on_delete=models.CASCADE, related_name="exams")
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"{self.exam_category} ({self.start_date} to {self.end_date})"
