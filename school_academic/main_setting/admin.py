from django.contrib import admin
from .models import Department, SubjectConfig

class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name',)  # Display the name field in the list view
    search_fields = ('name',)  # Allow searching by name
    ordering = ('name',)  # Order the list by name

admin.site.register(Department, DepartmentAdmin)

from .models import Programme

class ProgramAdmin(admin.ModelAdmin):
    list_display = ('name',)  # Display the name field in the list view
    search_fields = ('name',)  # Allow searching by name
    ordering = ('name',)  # Order the list by name

admin.site.register(Programme, ProgramAdmin)

from .models import Subject
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('subject_code', 'subject_name','status','department')  # Display relevant fields
    search_fields = ('subject_code', 'subject_name')  # Allow searching by subject code and name
    ordering = ('subject_name',)  # Order the list by subject name

admin.site.register(Subject, SubjectAdmin)

from .models import Class

class ClassAdmin(admin.ModelAdmin):
    list_display = ('programme', 'class_name', 'no_of_stream', 'view_assigned_streams')
    filter_horizontal = ('assigned_streams',)  # Enables a user-friendly interface for selecting streams

admin.site.register(Class, ClassAdmin)# Order the list by program and class names


from .models import Term

class TermAdmin(admin.ModelAdmin):
    list_display = ('name',)  # Display the name field in the list view
    search_fields = ('name',)  # Allow searching by term name
    ordering = ('name',)  # Order the list by term name

# Register the Term model with the admin site
admin.site.register(Term, TermAdmin)

from .models import AcademicYear

class AcademicYearAdmin(admin.ModelAdmin):
    list_display = ('name', 'status')  # Display name and status in the list view
    search_fields = ('name',)  # Allow searching by name
    ordering = ('name',)  # Order by name

# Register the AcademicYear model with the admin site
admin.site.register(AcademicYear, AcademicYearAdmin)

from .models import Assessment

class AssessmentAdmin(admin.ModelAdmin):
    list_display = ('name',)  # Display the name field in the list view
    search_fields = ('name',)  # Allow searching by name
    ordering = ('name',)  # Order by name

# Register the Assessment model with the admin site
admin.site.register(Assessment, AssessmentAdmin)

from django.contrib import admin
from .models import Stream

@admin.register(Stream)
class StreamAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)



class SubjectConfigAdmin(admin.ModelAdmin):
    list_display = ('class_name', 'get_assigned_streams', 'no_of_assigned_subjects', 'get_subjects')
    search_fields = ('class_name__class_name',)  # Search by class name
    filter_horizontal = ('assigned_streams', 'subjects')

    def get_assigned_streams(self, obj):
        return ", ".join([stream.name for stream in obj.assigned_streams.all()])
    get_assigned_streams.short_description = 'Assigned Streams'  # Name displayed in the admin

    def get_subjects(self, obj):
        return ", ".join([subject.subject_name for subject in obj.subjects.all()])
    get_subjects.short_description = 'Subjects'  # Name displayed in the admin

admin.site.register(SubjectConfig, SubjectConfigAdmin)



# systemUsers/admin.py
from django.contrib import admin
from .models import SubjectAllocation

class SubjectAllocationAdmin(admin.ModelAdmin):
    list_display = (
        'academic_year', 
        'term', 
        'subject', 
        'class_name', 
        'teacher_full_name',  # Display teacher's full name
        'phone_number',       # Display teacher's phone number
        'assigned_date', 
        'status'
    )
    search_fields = (
        'subject__name', 
        'class_name__class_name', 
        'teacher__full_name', 
        'phone_number'
    )
    
    # Method to display teacher's full name in the admin list view
    @admin.display(description='Full Name')
    def teacher_full_name(self, obj):
        return obj.teacher.full_name
    
    # Method to display teacher's phone number in the admin list view
    @admin.display(description='Phone Number')
    def phone_number(self, obj):
        return obj.teacher.phone_number

admin.site.register(SubjectAllocation, SubjectAllocationAdmin)


# systemUsers/admin.py
from django.contrib import admin
from .models import ResultsDeadline  # Import ResultsDeadline model

class ResultsDeadlineAdmin(admin.ModelAdmin):
    list_display = ('program_name', 'deadline_date')
    search_fields = ('program_name__name',)  # Assuming Programme model has a 'name' field

admin.site.register(ResultsDeadline, ResultsDeadlineAdmin)

# systemUsers/admin.py
from django.contrib import admin
from .models import Publish  # Import Publish model

class PublishAdmin(admin.ModelAdmin):
    list_display = ('program_name', 'action')
    list_filter = ('action',)
    search_fields = ('program_name__name',)  # Assuming Programme model has a 'name' field

admin.site.register(Publish, PublishAdmin)
