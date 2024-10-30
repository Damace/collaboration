# admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, StudentProfile, TeacherProfile, AcademicProfile, AdmissionProfile, PrincipalProfile, AdministratorProfile

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    # list_display = ('username', 'email', 'first_name', 'last_name', 'role', 'is_staff')

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(StudentProfile)
admin.site.register(TeacherProfile)
admin.site.register(AcademicProfile)
admin.site.register(AdmissionProfile)
admin.site.register(PrincipalProfile)
admin.site.register(AdministratorProfile)
