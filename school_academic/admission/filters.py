# systemUsers/filters.py

import django_filters
from main_setting.models import AcademicYear, Class, Programme, Stream, Term
from admission.models import StudentRegistration


class StudentFilter(django_filters.FilterSet):
    academic_year = django_filters.ModelChoiceFilter(queryset=AcademicYear.objects.all())
    term = django_filters.ModelChoiceFilter(queryset=Term.objects.all())
    programme = django_filters.ModelChoiceFilter(queryset=Programme.objects.all())
    student_class = django_filters.ModelChoiceFilter(queryset=Class.objects.all())
    class_stream = django_filters.ModelChoiceFilter(queryset=Stream.objects.all())

    class Meta:
        model = StudentRegistration # Replace with your actual Student model
        fields = [
            'academic_year',
            'term',
            'programme',
            'student_class',
            'class_stream',
        ]

