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
        verbose_name = "Character assessments"
        verbose_name_plural = "Character assessments"


class StudentsresultsProxy(StudentRegistration):
    class Meta:
        proxy = True
        verbose_name = "Students Results"
        verbose_name_plural = "Students Results"




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

class StudentsResult(models.Model):
    registration_number = models.CharField(max_length=50)
    entry_year = models.CharField(max_length=20)
    entry_term = models.CharField(max_length=20)
    entry_programme = models.CharField(max_length=100)
    entry_class = models.CharField(max_length=50)
    stream_name = models.CharField(max_length=50)
    full_name = models.CharField(max_length=100)
    subject_code = models.CharField(max_length=100)
    subject_name = models.CharField(max_length=100)
    te = models.CharField(max_length=10,default=0)
    ane = models.CharField(max_length=10,default=0)
    mtt2 = models.CharField(max_length=10,default=0)
    mtt1 = models.CharField(max_length=10,default=0)
    mte = models.CharField(max_length=10,default=0)
    average = models.CharField(null=True, blank=True, max_length=10)
    grade = models.CharField(max_length=2, null=True)
    remark = models.CharField(null=True, blank=True, max_length=10)
    position = models.IntegerField(null=True, blank=True)
    result_summary = models.CharField(max_length=200)
    
    class Meta:
        verbose_name = "Edit Results"
        verbose_name_plural = "Edit Results"
    
    def __str__(self):
        return f"{self.full_name} - {self.subject_name}"
    
    
    
from django.db import models

class StudentsResultQue(models.Model):
    registration_number = models.CharField(max_length=50, null=True)
    entry_year = models.CharField(max_length=20, null=True)
    entry_term = models.CharField(max_length=20, null=True)
    entry_programme = models.CharField(max_length=100, null=True)
    entry_class = models.CharField(max_length=50, null=True)
    stream_name = models.CharField(max_length=50, null=True)
    full_name = models.CharField(max_length=100, null=True)
    subject_code = models.CharField(max_length=100, null=True)
    subject_name = models.CharField(max_length=100, null=True)
    mt3 = models.FloatField(null=True)
    mt4 = models.FloatField(null=True)
    mte2 = models.FloatField(null=True)
    ae = models.FloatField(null=True)
    hpbt1 = models.FloatField(null=True)
    hpbt2 = models.FloatField(null=True)
    hpbt3 = models.FloatField(null=True)
    average = models.FloatField(null=True)
    grade = models.CharField(max_length=2, null=True)
    remark = models.CharField(max_length=100, null=True)
    position = models.IntegerField(null=True)
    
    def __str__(self):
        return f"{self.full_name} - {self.subject_name} ({self.entry_year} - {self.entry_term})"


class ClassResults(models.Model):
    registration_number = models.CharField(max_length=50)
    academic_year = models.CharField(max_length=50)
    term = models.CharField(max_length=50)
    entry_programme = models.CharField(max_length=100)
    entry_class = models.CharField(max_length=50)
    stream_name = models.CharField(max_length=50)
    stream_name = models.CharField(max_length=50)
    full_name = models.CharField(max_length=100)
    subjects = models.TextField()  
    scores = models.TextField()
    te = models.CharField(max_length=100)
    ane = models.CharField(max_length=100)
    mtt2 = models.CharField(max_length=100)
    mtt1 = models.CharField(max_length=100)
    mte = models.CharField(max_length=100)
    average = models.FloatField(max_length=100)
    grade = models.CharField(max_length=2)
    remark = models.CharField(max_length=100)
    position = models.IntegerField()
    
    
class StudentAssessments(models.Model):
    student = models.CharField(max_length=50)
    registration_number = models.CharField(max_length=50)
    full_name = models.CharField(max_length=100)
    entry_year = models.CharField(max_length=20)
    entry_term = models.CharField(max_length=20)
    entry_programme = models.CharField(max_length=50)
    entry_class = models.CharField(max_length=50)
    stream_name = models.CharField(max_length=50)
    assessment_name = models.CharField(max_length=100)
    grade = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.full_name} - {self.assessment_name} ({self.grade})"
