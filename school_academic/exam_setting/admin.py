# admin.py
from django.contrib import admin
from .models import GradeScale

class GradeScaleAdmin(admin.ModelAdmin):
    list_display = ('program_name', 'grade_name', 'minimum_marks', 'grade_point', 'remark', 'sequence_order')
    search_fields = ('grade_name', 'program_name__name')  # Allow searching by grade name and program name
    ordering = ('sequence_order',)  # Order by sequence order

class ProgramAdmin(admin.ModelAdmin):
    list_display = ('name',)

# Register the models with the admin site
admin.site.register(GradeScale, GradeScaleAdmin)

from .models import GradeDivision

class GradeDivisionAdmin(admin.ModelAdmin):
    list_display = ('program_name', 'grade_name', 'division_title', 'minimum_division_point', 'sequence_order')
    search_fields = ('grade_name', 'division_title', 'program_name__name')  # Allow searching by relevant fields
    ordering = ('sequence_order',)  # Order by sequence order

class ProgramAdmin(admin.ModelAdmin):
    list_display = ('name',)

# Register the models with the admin site
admin.site.register(GradeDivision, GradeDivisionAdmin)

from .models import ExamsCategory

class ExamsCategoryAdmin(admin.ModelAdmin):
    list_display = ('short_name', 'name', 'mandatory')
    search_fields = ('short_name', 'name')  # Allow searching by short name and name
    list_filter = ('mandatory',)  # Filter by mandatory status

# Register the ExamsCategory model with the admin site
admin.site.register(ExamsCategory, ExamsCategoryAdmin)