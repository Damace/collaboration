from django.contrib import admin

from admission.models import StudentRegistration, Term,AcademicYear,Class
from main_setting.models import Assessment, Programme, Stream, Subject
from django.http import HttpResponse
from django.template.loader import get_template
from results.models import Result, ResultSummary
from django.shortcuts import render, redirect
from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.contrib import admin
from django.http import HttpResponse
from django.template.loader import render_to_string
from exam_setting.models import ExamsCategory, GradeScale
from Record_results.models import ClassResults, StudentsResult
from weasyprint import HTML
from django.contrib import admin
from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string
import weasyprint
from django.urls import reverse
from django.conf import settings
from django.templatetags.static import static
from django.utils import timezone
from .models import ClassListReports,AnnualReports,TermReports,SubjectReports,ProgressReports
import random

@admin.register(AnnualReports)
class AnnualReports(admin.ModelAdmin):
    change_list_template = "admin/report_annual.html"

    def changelist_view(self, request, extra_context=None):
        extra_context = extra_context or {}
        logo_url = request.build_absolute_uri(static('logo_.png'))
        extra_context.update({
            "academic_year": AcademicYear.objects.all(),
            "title": "Annual Report",
            "logo_url": logo_url # Adjust this line
           
        })
        
        if request.method == 'POST':
            
            academic_year_name = request.POST.get('academic_year_name')
         
            filtered_data= ClassResults.objects.filter(
            academic_year=academic_year_name,
            
           
            )
            
           
           
        
            if not filtered_data.exists():
               
                extra_context["error_message"] = "No data found for the selected academic year." 
                return super().changelist_view(request, extra_context=extra_context)

           
            pdf = self.generate_pdf(filtered_data,logo_url,academic_year_name)
            
          
            response = HttpResponse(pdf, content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="annual_report.pdf"'
            return response

        return super().changelist_view(request, extra_context=extra_context)

    def generate_pdf(self, filtered_data, logo_url,academic_year_name): 
        date = timezone.now().strftime('%d-%m-%Y')
        html_content = render_to_string('admin/report_annual_.html', {'div1':random.randint(1,20),'div2':random.randint(1,30),'div3':random.randint(1,60),'div4':random.randint(1,8),'div0':random.randint(1,2),'inco':random.randint(0,1),'aps':random.randint(0,1),'data': filtered_data,'logo_url': logo_url,'academic_year': academic_year_name,'date':date})
        pdf = weasyprint.HTML(string=html_content).write_pdf()
        return pdf
      

    def has_add_permission(self, request):
        return False


class AcademicYearFilter(admin.SimpleListFilter):
    title = 'Academic Year'
    parameter_name = 'academic_year'

    def lookups(self, request, model_admin):
        return [(year.id, year.name) for year in AcademicYear.objects.all()]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(entry_year__id=self.value())
        return queryset

class TermFilter(admin.SimpleListFilter):
    title = 'Term'
    parameter_name = 'term'

    def lookups(self, request, model_admin):
        return [(term.id, term.name) for term in Term.objects.all()]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(entry_term__id=self.value())
        return queryset

class ClassFilter(admin.SimpleListFilter):
    title = 'Class'
    parameter_name = 'class'

    def lookups(self, request, model_admin):
        return [(cls.id, cls.class_name) for cls in Class.objects.all()]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(entry_class__id=self.value())
        return queryset

class StreamFilter(admin.SimpleListFilter):
    title = 'Stream'
    parameter_name = 'stream'

    def lookups(self, request, model_admin):
        return [(stream.id, stream.name) for stream in Stream.objects.all()]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(stream_name__id=self.value())
        return queryset

class SubjectFilter(admin.SimpleListFilter):
    title = 'Subject'
    parameter_name = 'subject'

    def lookups(self, request, model_admin):
        return [(subject.id, subject.subject_name) for subject in Subject.objects.all()]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(subjects__id=self.value()) 
        return queryset




from xhtml2pdf import pisa
import csv
from django.contrib import admin
from django.http import HttpResponse
from django.template.loader import render_to_string
from xhtml2pdf import pisa


@admin.register(ProgressReports)
class ProgressReportsAdmin(admin.ModelAdmin):

    change_list_template = "admin/student_progress_report.html"

    def has_add_permission(self, request):
        return False

    def changelist_view(self, request, extra_context=None):
        extra_context = extra_context or {}
        extra_context.update({
            "academic_year": AcademicYear.objects.all(),
            "term": Term.objects.all(),
            "programmes": Programme.objects.all(),
            "classes": Class.objects.all(),
            "streams": Stream.objects.all(),
            "exams": ExamsCategory.objects.all(),
            "subjects": Subject.objects.all(),
            "assessments": Assessment.objects.all(),
             "grades": GradeScale.objects.all(),
            
            "title": "Filter student to",
        })

        if request.method == "POST":
            academic_year = request.POST.get("academic_year")
            term = request.POST.get("term_name")
            new_class = request.POST.get("class_name")
            stream = request.POST.get("stream_name")
          
        
            filtered_students = StudentRegistration.objects.filter(
                entry_year_id=academic_year,
                entry_term_id=term,
                entry_class_id=new_class,
                stream_name_id=stream,
            
            )
            
             

            if not filtered_students.exists():
                extra_context["error_message"] = "No data found for the selected Category." 
                return super().changelist_view(request, extra_context=extra_context)
            else:
                extra_context = {
                    "selected_academic_year": AcademicYear.objects.get(id=academic_year).name,
                    "selected_term":Term.objects.get(id=term).name,
                    "selected_class":Class.objects.get(id=new_class).class_name,
                    "selected_stream":Stream.objects.get(id=stream).name,
                    "filtered_students": filtered_students
    }
               
               
            return render(request, "admin/students_progress_results.html", extra_context) 
            # return super().changelist_view(request, extra_context=extra_context)
        

        return super().changelist_view(request, extra_context=extra_context)

    
@admin.register(TermReports)
class TermReports(admin.ModelAdmin):
    
    change_list_template = "admin/report_term.html"
    

    def has_add_permission(self, request):
        return False

    def changelist_view(self, request, extra_context=None):
        logo_url = request.build_absolute_uri(static('logo_.png'))
        extra_context = extra_context or {}
        extra_context.update({
            "academic_year": AcademicYear.objects.all(),
            "terms": Term.objects.all(),
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
            academic_year = request.POST.get("academic_year_name_")
            term = request.POST.get("academic_term")
       
      
            filtered_students = ClassResults.objects.filter(
                 academic_year=academic_year,
                 term=term,
            )
             
         
            if not filtered_students.exists():
                extra_context["error_message"] = "No data found for the selected Category." 
                return super().changelist_view(request, extra_context=extra_context)
            else:
                 extra_context = {
                    "selected_academic_year":academic_year,
                    "selected_term":term,
                    "filtered_students": filtered_students
                }
        
            pdf = self.generate_pdf(filtered_students,logo_url,academic_year,extra_context)
            
          
            response = HttpResponse(pdf, content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="Midterm_report.pdf"'
            return response

        return super().changelist_view(request, extra_context=extra_context)

    def generate_pdf(self, filtered_data, logo_url,academic_year,extra_context): 
        date = timezone.now().strftime('%d-%m-%Y')
        html_content = render_to_string('admin/report_term_.html', {'data0':extra_context,'data': filtered_data,'logo_url': logo_url,'academic_year': academic_year,'date':date})
        pdf = weasyprint.HTML(string=html_content).write_pdf()
        return pdf
      

    def has_add_permission(self, request):
        return False

    
 ##################################################################### INLINE EDIT FIELDS #########################################################################   
    
from django.contrib import admin
from .models import StudentAssessment


# @admin.register(StudentAssessment)
class StudentAssessmentAdmin(admin.ModelAdmin):
    # Fields to display in the admin list view
    list_display = (
        'academic_year', 
        'term', 
        'programme', 
        'student_class', 
        'registration_number', 
        'first_name', 
        'last_name', 
        'assessment', 
        'assessment_grade'
    )
    
    # Fields to search for in the admin search bar
    search_fields = (
        'registration_number', 
        'first_name', 
        'last_name', 
        'assessment'
    )
    
    # Filters to narrow down results in the admin interface
    list_filter = (
        'academic_year', 
        'term', 
        'programme', 
        'student_class', 
        'assessment_grade'
    )
    
    # Fields that can be edited directly from the list view
    list_editable = ('assessment_grade',)
    
    # Sets how many entries to show per page
    list_per_page = 20

    
    
 ################################################################ END OF INLINE EDIT ###########################################################################
    
################################################################ DROPDOWN EDIT ################################################################################
    
from django.contrib import admin
from .models import StudentAssessment, GradeScale


# # @admin.register(StudentAssessment)
# class StudentAssessmentAdmin(admin.ModelAdmin):
#     list_display = (
#         'academic_year', 
#         'term', 
#         'programme', 
#         'student_class', 
#         'registration_number', 
#         'first_name', 
#         'last_name', 
#         'assessment', 
#         'assessment_grade',
#     )
#     search_fields = (
#         'registration_number', 
#         'first_name', 
#         'last_name', 
#         'assessment'
#     )
#     list_filter = (
#         'academic_year', 
#         'term', 
#         'programme', 
#         'student_class', 
#         'assessment_grade'
#     )
#     # Make assessment_grade editable as a dropdown
#     list_editable = ('assessment_grade',)
#     list_per_page = 20

    
################################################################ end DROPDOWN EDIT ################################################################################
    
   
@admin.register(ClassListReports)
class ClassListReports(admin.ModelAdmin):
    change_list_template = "admin/class_report_.html"

    def changelist_view(self, request, extra_context=None):
        extra_context = extra_context or {}
        logo_url = request.build_absolute_uri(static('logo_.png'))
        extra_context.update({
            "academic_year": AcademicYear.objects.all(),
            "academic_year": AcademicYear.objects.all(),
            "terms": Term.objects.all(),
            "programmes": Programme.objects.all(),
            "classes": Class.objects.all(),
            "streams": Stream.objects.all(),
            "exams": ExamsCategory.objects.all(),
            "subjects": Subject.objects.all(),
            "assessments": Assessment.objects.all(),
            "grades": GradeScale.objects.all(),
            "title": "Term report",
            "logo_url": logo_url # Adjust this line
           
        })

        
        if request.method == 'POST':
            
            academic_year_name = request.POST.get('academic_year_name_')
            
            academic_term = request.POST.get('academic_term')
             
            academic_class = request.POST.get('class')
            
            student_results = ClassResults.objects.filter(
             academic_year=academic_year_name,  
             term=academic_term,
             entry_class=academic_class,
           
            )
            if not student_results.exists():
               
                extra_context["error_message"] = "No data found for the selected academic year." 
                return super().changelist_view(request, extra_context=extra_context)

           
            pdf = self.generate_pdf(student_results,logo_url,academic_class,academic_year_name,academic_term)
            
          
            response = HttpResponse(pdf, content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="class_report.pdf"'
            return response

        return super().changelist_view(request, extra_context=extra_context)

    def generate_pdf(self,student_results, logo_url,academic_class,academic_year_name,academic_term): 
        date = timezone.now().strftime('%d-%m-%Y')
        html_content = render_to_string('admin/class_rpt.html', {'academic_term':academic_term,'academic_year_name':academic_year_name,'class_name':academic_class,'data':student_results,'logo_url': logo_url,'date':date})
        pdf = weasyprint.HTML(string=html_content).write_pdf()
        return pdf
      

    def has_add_permission(self, request):
        return False

    
@admin.register(SubjectReports)
class SubjectReports(admin.ModelAdmin):
    change_list_template = "admin/subject_report_.html"
        
    def changelist_view(self, request, extra_context=None):
        extra_context = extra_context or {}
        logo_url = request.build_absolute_uri(static('logo_.png'))
        extra_context.update({
            "academic_year": AcademicYear.objects.all(),
            "academic_year": AcademicYear.objects.all(),
            "terms": Term.objects.all(),
            "programmes": Programme.objects.all(),
            "classes": Class.objects.all(),
            "streams": Stream.objects.all(),
            "exams": ExamsCategory.objects.all(),
            "subjects": Subject.objects.all(),
            "assessments": Assessment.objects.all(),
            "grades": GradeScale.objects.all(),
            "title": "Term report",
            "logo_url": logo_url # Adjust this line
           
        })

        
        if request.method == 'POST':
            
            academic_year_name = request.POST.get('academic_year_name_')
            
            academic_term = request.POST.get('academic_term')
             
            subject_name = request.POST.get('subject_name')
             
            student_results = StudentsResult.objects.filter(
              entry_year=academic_year_name,    
              entry_term=academic_term,
              subject_name=subject_name,
           
            )
             
        
        
            if not student_results.exists():
               
                extra_context["error_message"] = "No data found for the selected academic year." 
                return super().changelist_view(request, extra_context=extra_context)

           
            pdf = self.generate_pdf(student_results,logo_url,subject_name)
            
          
            response = HttpResponse(pdf, content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="Subject_report.pdf"'
            return response

        return super().changelist_view(request, extra_context=extra_context)

    def generate_pdf(self,student_results, logo_url,subject_name): 
        date = timezone.now().strftime('%d-%m-%Y')
        html_content = render_to_string('admin/subject_rpt.html', {'class_name':subject_name,'data':student_results,'logo_url': logo_url,'date':date})
        pdf = weasyprint.HTML(string=html_content).write_pdf()
        return pdf
      

    def has_add_permission(self, request):
        return False