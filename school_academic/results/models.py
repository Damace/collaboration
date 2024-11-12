from django.db import models

from admission.models import StudentRegistration

from django.db import models

from main_setting.models import AcademicYear, Class, Subject, Term
from exam_setting.models import SetExam

# class Result(models.Model):
#     GENDER_CHOICES = [
#         ('Male', 'Male'),
#         ('Female', 'Female'),
#     ]

#     full_name = models.ForeignKey(StudentRegistration, on_delete=models.CASCADE, related_name="results")
#     gender = models.CharField(max_length=100, choices=GENDER_CHOICES, default='Female')
#     class_name = models.CharField(max_length=100)
#     subjects_name = models.CharField(max_length=100)
#     subjects_number = models.CharField(max_length=100)
#     total = models.CharField(max_length=100)
#     avg = models.CharField(max_length=100)
#     grade = models.CharField(max_length=2)
#     point = models.CharField(max_length=10)
#     division = models.CharField(max_length=10)
#     comb_pos = models.CharField(max_length=10)
#     class_pos = models.CharField(max_length=10)

#     def __str__(self):
#         return f"{self.full_name.registration_number} - {self.subjects_name} - {self.division}"


# class Result(models.Model):
#     academic_year = models.ForeignKey(AcademicYear, on_delete=models.CASCADE)
#     term = models.ForeignKey(Term, on_delete=models.CASCADE)
#     registration_number = models.CharField(max_length=100)
#     full_name = models.ForeignKey(StudentRegistration, on_delete=models.CASCADE, related_name="results")
#     class_name = models.ForeignKey(Class, on_delete=models.CASCADE)  # Replaces char field with a ForeignKey
#     subject = models.ForeignKey(Subject, on_delete=models.CASCADE)  # Links directly to Subject model
#     total = models.DecimalField(max_digits=5, decimal_places=2)
#     avg = models.DecimalField(max_digits=4, decimal_places=2)
#     grade = models.CharField(max_length=2)
#     point = models.DecimalField(max_digits=4, decimal_places=2)
#     division = models.CharField(max_length=10)
#     comb_pos = models.CharField(max_length=10)
#     class_pos = models.CharField(max_length=10)

#     def __str__(self):
#         return f"{self.full_name.registration_number} - {self.subject.subject_code} - {self.division}"


class Result(models.Model):
    academic_year = models.CharField(max_length=100)
    term = models.CharField(max_length=100)
    exam_type = models.CharField(max_length=100,editable=False)
    registration_number = models.CharField(max_length=100)
    full_name = models.CharField(max_length=100)
    class_name = models.CharField(null=True,max_length=100) # Replaces char field with a ForeignKey
    subject = models.CharField(null=True,max_length=100)  # Links directly to Subject model
    total = models.DecimalField(null=True,max_digits=5, decimal_places=2)
    avg = models.DecimalField(null=True,max_digits=4, decimal_places=2)
    grade = models.CharField(null=True,max_length=2)
    point = models.DecimalField(null=True,max_digits=4, decimal_places=2)
    division = models.CharField(null=True,max_length=10)
    comb_pos = models.CharField(null=True,max_length=10)
    class_pos = models.CharField(null=True,max_length=10)
    
    class Meta:
        verbose_name = "Exam Result"
        verbose_name_plural = "Exam Results"

    def __str__(self):
        return f"{self.full_name} - {self.subject} - {self.division}"
    
    


from django.db import models

class ExamResults(models.Model):
    """Empty model for Exam Results."""

    class Meta:
        verbose_name = "Exam Result"
        verbose_name_plural = "Exam Results"

    pass


from django.db import models



class ExaminationResult(SetExam):
      exam_type = models.CharField(max_length=100)
       
      class Meta:
        verbose_name = "Examination Result"
        verbose_name_plural = "Examination Result"



class ResultSummary(models.Model):
    academic_year = models.CharField(max_length=20)
    term = models.CharField(max_length=20)
    exam_type = models.CharField(max_length=20)
    registration_number = models.CharField(max_length=20)
    
    # Fields for each classification
    grade_I = models.PositiveIntegerField(default=0)       # Grade I count
    grade_II = models.PositiveIntegerField(default=0)      # Grade II count
    grade_III = models.PositiveIntegerField(default=0)     # Grade III count
    grade_IV = models.PositiveIntegerField(default=0)      # Grade IV count
    grade_0 = models.PositiveIntegerField(default=0)       # Failed count
    incomplete = models.PositiveIntegerField(default=0)    # INC (Incomplete)
    absent = models.PositiveIntegerField(default=0)        # ABS (Absent)

    def __str__(self):
        return f"Result Summary for {self.registration_number} - {self.academic_year.name} {self.term.name}"

