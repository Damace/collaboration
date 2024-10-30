# systemUsers/models.py
from django.db import models

from main_setting.models import AcademicYear, Class, Stream, Subject, Term
from exam_setting.models import ExamsCategory

class EnterResults(models.Model):
    academic_year = models.ForeignKey(AcademicYear, on_delete=models.CASCADE)
    term = models.ForeignKey(Term, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    exam_category = models.ForeignKey(ExamsCategory, on_delete=models.CASCADE)
    class_name = models.ForeignKey(Class, on_delete=models.CASCADE)  # ForeignKey to Class
    stream = models.ForeignKey(Stream, on_delete=models.CASCADE)  # ForeignKey to Stream
    
    def __str__(self):
        return f'Results for {self.subject} - {self.class_name} - {self.stream} - {self.academic_year}'
