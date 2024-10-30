from django import forms
from .models import CustomUser, Student, Teacher, Academic, Admission, Principal, Administrator

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['username', 'email', 'first_name', 'last_name', 'phone_number', 'address', 'profile_picture', 'student_id', 'date_of_birth', 'student_class']

class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['username', 'email', 'first_name', 'last_name', 'phone_number', 'address', 'profile_picture', 'teacher_id', 'department']

class AcademicForm(forms.ModelForm):
    class Meta:
        model = Academic
        fields = ['username', 'email', 'first_name', 'last_name', 'phone_number', 'address', 'profile_picture', 'academic_id']

class AdmissionForm(forms.ModelForm):
    class Meta:
        model = Admission
        fields = ['username', 'email', 'first_name', 'last_name', 'phone_number', 'address', 'profile_picture', 'admission_id']

class PrincipalForm(forms.ModelForm):
    class Meta:
        model = Principal
        fields = ['username', 'email', 'first_name', 'last_name', 'phone_number', 'address', 'profile_picture', 'principal_id']

class AdministratorForm(forms.ModelForm):
    class Meta:
        model = Administrator
        fields = ['username', 'email', 'first_name', 'last_name', 'phone_number', 'address', 'profile_picture', 'administrator_id']
