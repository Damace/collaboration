# systemUsers/admin.py
from django.contrib import admin
from django import forms

from Record_results.models import EnterResults, StudentsProxy
from main_setting.models import Assessment, Programme, Stream, Subject, SubjectAllocation, SubjectConfig
from admission.models import StudentRegistration
from exam_setting.models import ExamsCategory, GradeScale
# from models import EnterResults, Stream, StudentsProxy
from django.urls import path, reverse
from django.utils.html import format_html
from django.shortcuts import redirect, render
from django.contrib import messages




from django.contrib import admin
from .models import AcademicYear, QueResults, StudentsAssasmentsProxy, Term, Class, Stream, StudentsProxy
from django.shortcuts import render, redirect
from .models import QueResults

class StudentsProxyAdmin(admin.ModelAdmin):
    change_list_template = "admin/filter_resultStudent.html"

    def has_add_permission(self, request):
        return False

    def changelist_view(self, request, extra_context=None):
        extra_context = extra_context or {}
        extra_context.update({
            "academic_year": AcademicYear.objects.all(),
            "term": Term.objects.all(),
            "programmes": Programme.objects.all(),
            "classes": Class.objects.all(),
            "stream": Stream.objects.all(),
            "exams": ExamsCategory.objects.all(),
            "subjects": Subject.objects.all(),
            "title": "Filter student to",
        })

        if request.method == "POST":
            academic_year = request.POST.get("academic_year")
            term = request.POST.get("term")
            programme = request.POST.get("programme")
            new_class = request.POST.get("new_class")
            stream = request.POST.get("stream")
            exam = request.POST.get("exam")
            subject = request.POST.get("subject")
            
            # print( academic_year,term,programme,new_class,stream,subject)

            filtered_students = StudentRegistration.objects.filter(
                entry_year=academic_year,
                entry_term=term,
                entry_programme=programme,
                entry_class=new_class,
                stream_name=stream,
                subjects=subject,
            )
             

            if not filtered_students.exists():
                extra_context["error_message"] = "There is no Students name in those categories." 
                return super().changelist_view(request, extra_context=extra_context)
            else:
                # If students are found, pass them to the template
                extra_context["selected_academic_year"] = AcademicYear.objects.get(id=academic_year).name
                extra_context["selected_term"] = Term.objects.get(id=term).name
                extra_context["selected_programme"] = Programme.objects.get(id=programme).name
                extra_context["selected_class"] = Class.objects.get(id=new_class).class_name
                extra_context["selected_stream"] = Stream.objects.get(id=stream).name
                extra_context["selected_subject"] = Subject.objects.get(id=subject).subject_name
                extra_context["selected_subject_code"] = Subject.objects.get(id=subject).subject_code
                extra_context["filtered_students"] = filtered_students
                extra_context["subject"] = subject
                extra_context["selected_exams"] =  exam
                extra_context["filtered_students"] = filtered_students
               
                return render(request, "admin/student_results.html", extra_context) 
            # return super().changelist_view(request, extra_context=extra_context)
        

        return super().changelist_view(request, extra_context=extra_context)


    # Render the form with filtered students if not a POST request
    #   return render(request, 'addresults.html', {'filtered_students': filtered_students})


admin.site.register(StudentsProxy, StudentsProxyAdmin)


from django.contrib import admin
from .models import QueResults

class BaseFilter(admin.SimpleListFilter):
    def lookups(self, request, model_admin):
        values = set(self.get_values(model_admin.model))
        return [(value, value) for value in values]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(**{self.parameter_name: self.value()})
        return queryset

class AcademicYearFilter(BaseFilter):
    title = 'Academic Year'
    parameter_name = 'academic_year'

    def get_values(self, model):
        return model.objects.values_list('academic_year', flat=True)

class TermFilter(BaseFilter):
    title = 'Term'
    parameter_name = 'term'

    def get_values(self, model):
        return model.objects.values_list('term', flat=True)

class ProgrammeFilter(BaseFilter):
    title = 'Programme'
    parameter_name = 'programme'

    def get_values(self, model):
        return model.objects.values_list('programme', flat=True)

class ClassNameFilter(BaseFilter):
    title = 'Class Name'
    parameter_name = 'class_name'

    def get_values(self, model):
        return model.objects.values_list('class_name', flat=True)

class StreamFilter(BaseFilter):
    title = 'Stream'
    parameter_name = 'stream'

    def get_values(self, model):
        return model.objects.values_list('stream', flat=True)

class ExamTypeFilter(BaseFilter):
    title = 'Exam Type'
    parameter_name = 'exam_type'

    def get_values(self, model):
        return model.objects.values_list('exam_type', flat=True)

class SubjectFilter(BaseFilter):
    title = 'Subject'
    parameter_name = 'subject'

    def get_values(self, model):
        return model.objects.values_list('subject', flat=True)

class ResultSummaryFilter(BaseFilter):
    title = 'Result Summary'
    parameter_name = 'result_summary'

    def get_values(self, model):
        return model.objects.values_list('result_summary', flat=True)


# @admin.register(QueResults)
class QueResultsAdmin(admin.ModelAdmin):
    list_display = ('registration_number', 'student_name', 'class_name', 'subject', 'result')
    list_filter = (
        AcademicYearFilter,
        TermFilter,
        ProgrammeFilter,
        ClassNameFilter,
        ExamTypeFilter,
        SubjectFilter,
     
    )
    search_fields = ('registration_number', 'student_name', 'class_name', 'subject__subject_name')
    def has_add_permission(self, request):
        return False




from django.contrib import admin
from .models import StudentsAssasmentsProxy

class StudentsAssessmentsProxyAdmin(admin.ModelAdmin):

    change_list_template = "admin/report_progress.html"

    def has_add_permission(self, request):
        return False

    def changelist_view(self, request, extra_context=None):
        extra_context = extra_context or {}
        extra_context.update({
            "academic_year": AcademicYear.objects.all(),
            "term": Term.objects.all(),
            "programmes": Programme.objects.all(),
            "classes": Class.objects.all(),
            "stream": Stream.objects.all(),
            "exams": ExamsCategory.objects.all(),
            "subjects": Subject.objects.all(),
            "assessments": Assessment.objects.all(),
             "grades": GradeScale.objects.all(),
            
            "title": "Filter student to",
        })

        if request.method == "POST":
            academic_year = request.POST.get("academic_year")
            term = request.POST.get("term")
            programme = request.POST.get("programme")
            new_class = request.POST.get("new_class")
            stream = request.POST.get("stream")
          
            
            # print('#######################################', academic_year,term,programme,new_class,stream,subject)

            filtered_students = StudentRegistration.objects.filter(
                entry_year=academic_year,
                entry_term=term,
                entry_programme=programme,
                entry_class=new_class,
                stream_name=stream,
            
            )
             

            if not filtered_students.exists():
                extra_context["error_message"] = "No data found for the selected Categor." 
                return super().changelist_view(request, extra_context=extra_context)
            else:
                # If students are found, pass them to the template
                extra_context["selected_academic_year"] = AcademicYear.objects.get(id=academic_year).name
                extra_context["selected_term"] = Term.objects.get(id=term).name
                extra_context["selected_programme"] = Programme.objects.get(id=programme).name
                extra_context["selected_class"] = Class.objects.get(id=new_class).class_name
                extra_context["selected_stream"] = Stream.objects.get(id=stream).name
                extra_context["filtered_students"] = filtered_students
                extra_context["filtered_students"] = filtered_students
               
                return render(request, "admin/students_assesments.html", extra_context) 
            # return super().changelist_view(request, extra_context=extra_context)
        

        return super().changelist_view(request, extra_context=extra_context)

 


admin.site.register(StudentsAssasmentsProxy, StudentsAssessmentsProxyAdmin)



from django.contrib import admin
from .models import StudentsresultsProxy  # Import the proxy model
from .models import StudentRegistration   # Import the original model

class StudentsresultsProxyAdmin(admin.ModelAdmin):
    
    change_list_template = "admin/report_progress.html"

    def has_add_permission(self, request):
        return False

    def changelist_view(self, request, extra_context=None):
        extra_context = extra_context or {}
        extra_context.update({
            "academic_year": AcademicYear.objects.all(),
            "term": Term.objects.all(),
            "programmes": Programme.objects.all(),
            "classes": Class.objects.all(),
            "stream": Stream.objects.all(),
            "exams": ExamsCategory.objects.all(),
            "subjects": Subject.objects.all(),
            "assessments": Assessment.objects.all(),
             "grades": GradeScale.objects.all(),
            
            "title": "Filter student to",
        })

        if request.method == "POST":
            academic_year = request.POST.get("academic_year")
            term = request.POST.get("term")
            programme = request.POST.get("programme")
            new_class = request.POST.get("new_class")
            stream = request.POST.get("stream")
          
            
            # print('#######################################', academic_year,term,programme,new_class,stream,subject)

            filtered_students = StudentRegistration.objects.filter(
                entry_year=academic_year,
                entry_term=term,
                entry_programme=programme,
                entry_class=new_class,
                stream_name=stream,
            
            )
             

            if not filtered_students.exists():
                extra_context["error_message"] = "No data found for the selected Categor." 
                return super().changelist_view(request, extra_context=extra_context)
            else:
                # If students are found, pass them to the template
                extra_context["selected_academic_year"] = AcademicYear.objects.get(id=academic_year).name
                extra_context["selected_term"] = Term.objects.get(id=term).name
                extra_context["selected_programme"] = Programme.objects.get(id=programme).name
                extra_context["selected_class"] = Class.objects.get(id=new_class).class_name
                extra_context["selected_stream"] = Stream.objects.get(id=stream).name
                extra_context["filtered_students"] = filtered_students
                extra_context["filtered_students"] = filtered_students
               
                return render(request, "admin/students_progress.html", extra_context) 
            # return super().changelist_view(request, extra_context=extra_context)
        

        return super().changelist_view(request, extra_context=extra_context)
   
# admin.site.register(StudentsresultsProxy, StudentsresultsProxyAdmin)



from django.contrib import admin
from .models import StudentsResultQue
from .forms import StudentsResultQueForm  # Import the custom form

class StudentsResultQueAdmin(admin.ModelAdmin):
    list_display = (
        # 'registration_number',
        # 'entry_year',
        # 'entry_term',
        # 'entry_programme',
        # 'entry_class',
        # 'stream_name',
        # 'full_name',
       'subject_code',
        'subject_name',
        'mt3',          # Add editable fields here
        'mt4',          # Add editable fields here
        'mte2',         # Add editable fields here
        'ae',           # Add editable fields here
        'hpbt1',        # Add editable fields here
        'hpbt2',        # Add editable fields here
        # 'hpbt3',        # Add editable fields here
        # 'average',
        # 'grade',
        # 'position',
    )
    list_filter = (
        'entry_year',
        'entry_term',
        'entry_programme',
        'entry_class',
        'stream_name',
        'subject_code',
        'subject_name',
        'full_name',
    )
    search_fields = ('registration_number', 'full_name', 'subject_name')
    ordering = ('-entry_year', 'full_name')
    list_per_page = 20

    # Add the editable fields
    list_editable = (
        'mt3',
        'mt4',
        'mte2',
        'ae',
        'hpbt1',
        'hpbt2',
        # 'hpbt3',
    )

    fieldsets = (
        (None, {
            'fields': (
                'registration_number',
                'entry_year',
                'entry_term',
                'entry_programme',
                'entry_class',
                'stream_name',
                'full_name',
                'subject_code',
                'subject_name',
                'mt3',
                'mt4',
                'mte2',
                'ae',
                'hpbt1',
                'hpbt2',
                'hpbt3',
                'average',
                'grade',
                'remark',
                'position',
            )
        }),
    )

# admin.site.register(StudentsResultQue, StudentsResultQueAdmin)


from django.contrib import admin
from .models import StudentsResult

class StudentsResultAdmin(admin.ModelAdmin):
    
    def has_add_permission(self, request):
        return False
    
    # Display fields in the admin list view
    list_display = ('registration_number', 'full_name','subject_code', 'subject_name','mt3', 'mt4', 'mte2', 'ae', 'hpbt1', 'hpbt2')
    
    # Search functionality
    search_fields = ('registration_number', 'full_name', 'subject_name')
    
    # Filtering options for the admin panel
    list_filter = ('entry_year', 'entry_term', 'entry_programme', 'entry_class', 'stream_name', 'grade')

    # Fieldsets for organizing fields in the admin form
    fieldsets = (
        (None, {
            'fields': ('registration_number', 'full_name','subject_code', 'subject_name')
        }),
        ('Exams Results', {
            'fields': ('mt3', 'mt4', 'mte2', 'ae', 'hpbt1', 'hpbt2', 'hpbt3', 'average', 'grade', 'remark'),
        }),
        ('Position', {
            'fields': ('position',),
        }),
        ('Meta Info', {
            'fields': ('entry_year', 'entry_term', 'entry_programme', 'entry_class', 'stream_name'),
            'classes': ('collapse',),
        }),
    )

    # Making fields editable from the list view for quick editing
    list_editable = ('mt3', 'mt4', 'mte2', 'ae', 'hpbt1', 'hpbt2')

    # Allow for inlines and customization as needed
    # You can also add actions like 'bulk update' or 'bulk delete' here.

# Register the model with the admin interface
admin.site.register(StudentsResult, StudentsResultAdmin)






