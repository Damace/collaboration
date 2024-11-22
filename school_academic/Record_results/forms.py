# forms.py
from django import forms

from admission.models import StudentRegistration
from .models import StudentsResultQue

class StudentsResultQueForm(forms.ModelForm):
    full_name = forms.ModelChoiceField(
        queryset=StudentRegistration.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        required=False,
        label="Student Full Name",
    )

    class Meta:
        model = StudentsResultQue
        fields = '__all__'
