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

            filtered_data = Result.objects.filter(academic_year=academic_year_name)
            filtered_data_2 = ResultSummary.objects.filter(academic_year=academic_year_name)
          
        
            if not filtered_data.exists():
               
                extra_context["error_message"] = "No data found for the selected academic year." 
                return super().changelist_view(request, extra_context=extra_context)

           
            pdf = self.generate_pdf(filtered_data,filtered_data_2,logo_url,academic_year_name)
            
          
            response = HttpResponse(pdf, content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="annual_report.pdf"'
            return response

        return super().changelist_view(request, extra_context=extra_context)

    def generate_pdf(self, filtered_data,filtered_data_2, logo_url,academic_year_name): 
        date = timezone.now().strftime('%d-%m-%Y')
        html_content = render_to_string('admin/report_annual_.html', {'data': filtered_data,'data2':filtered_data_2,'logo_url': logo_url,'academic_year': academic_year_name,'date':date})
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
        logo_url = request.build_absolute_uri(static('logo_.png'))
        profile_image = request.build_absolute_uri(static('profile.png'))
        
        
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
            reg_number = request.POST.get("reg_number")
            
           
            
            filtered_students = Result.objects.filter(registration_number=reg_number)
            filtered_students2 = StudentRegistration.objects.filter(registration_number=reg_number)
             

            if not filtered_students.exists():
                extra_context["error_message"] = "No Students with such Registration Number." 
                return super().changelist_view(request, extra_context=extra_context)
            else:
                extra_context["filtered_students"] = filtered_students
                extra_context["filtered_students2"] = filtered_students2
                
            pdf = self.generate_pdf(filtered_students,filtered_students2,logo_url,profile_image)
            
            response = HttpResponse(pdf, content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="annual_report.pdf"'
            return response

        return super().changelist_view(request, extra_context=extra_context)
        
    def generate_pdf(self, filtered_data,filtered_data_2, logo_url,profile_image): 
        date = timezone.now().strftime('%d-%m-%Y')
        html_content = render_to_string('admin/students_details.html', {'data': filtered_data,'data2':filtered_data_2,'logo_url': logo_url,'profile_image':profile_image,'date':date})
        pdf = weasyprint.HTML(string=html_content).write_pdf()
        return pdf
    
    def has_add_permission(self, request):
        return False
    



# @admin.register(TermReports)
# class TermReports(admin.ModelAdmin):
#     change_list_template = "admin/report_term.html"

#     def changelist_view(self, request, extra_context=None):
#         extra_context = extra_context or {}
#         logo_url =  request.build_absolute_uri(static('logo_.png')) 
#         extra_context.update({
#             "academic_year": AcademicYear.objects.all(),
#              "terms": Term.objects.all(),
#             "title": "Term Report",
#             "logo_url": logo_url  # Adjust this line
#         })
        
#         if request.method == 'POST':
            
#             academic_year = request.POST.get('academic_year')
#             academic_term = request.POST.get('academic_term')
            
#             filtered_data = Result.objects.filter(academic_year=academic_year, term=academic_term)
        
#             if not filtered_data.exists():
               
#                 extra_context["error_message"] = "No data found for the selected academic year and Term." 
#                 return super().changelist_view(request, extra_context=extra_context)

           
#             pdf = self.generate_pdf(filtered_data,logo_url)
            
          
#             response = HttpResponse(pdf, content_type='application/pdf')
#             response['Content-Disposition'] = 'attachment; filename="term_report.pdf"'
#             return response

#         return super().changelist_view(request, extra_context=extra_context)

#     def generate_pdf(self, filtered_data, logo_url,academic_year): 
#         academic_year_name = f'{'40000'}{academic_year}'
#         html_content = render_to_string('admin/report_term_.html', {'data': filtered_data,'logo_url': logo_url,'academic_year': academic_year_name})
#         pdf = weasyprint.HTML(string=html_content).write_pdf()
#         return pdf
    
    
    

#     def has_add_permission(self, request):
#         return False
    
# @admin.register(ClassListReports)
# class ClassListReports(admin.ModelAdmin):
#     change_list_template = "admin/report_annual.html"

#     def changelist_view(self, request, extra_context=None):
#         extra_context = extra_context or {}
#         logo_url =  request.build_absolute_uri(static('logo_.png')) 
#         extra_context.update({
#             "academic_year": AcademicYear.objects.all(),
#             "title": "Annual Report",
#             "logo_url": logo_url  # Adjust this line
#         })
        
#         if request.method == 'POST':
            
#             academic_year_name = request.POST.get('academic_year_name')

#             filtered_data = Result.objects.filter(academic_year=academic_year_name)
          
        
#             if not filtered_data.exists():
               
#                 extra_context["error_message"] = "No data found for the selected academic year." 
#                 return super().changelist_view(request, extra_context=extra_context)

           
#             pdf = self.generate_pdf(filtered_data,logo_url)
            
          
#             response = HttpResponse(pdf, content_type='application/pdf')
#             response['Content-Disposition'] = 'attachment; filename="annual_report.pdf"'
#             return response

#         return super().changelist_view(request, extra_context=extra_context)

#     def generate_pdf(self, filtered_data, logo_url,academic_year_name): 
#         html_content = render_to_string('admin/report_annual_.html', {'data': filtered_data,'logo_url': logo_url,'academic_year': academic_year_name})
#         pdf = weasyprint.HTML(string=html_content).write_pdf()
#         return pdf
    
    

#     def has_add_permission(self, request):
#         return False
    
# @admin.register(SubjectReports)
# class SubjectReports(admin.ModelAdmin):
#     change_list_template = "admin/report_annual.html"

#     def changelist_view(self, request, extra_context=None):
#         extra_context = extra_context or {}
#         logo_url =  request.build_absolute_uri(static('logo_.png')) 
#         extra_context.update({
#             "academic_year": AcademicYear.objects.all(),
#             "title": "Annual Report",
#             "logo_url": logo_url  # Adjust this line
#         })
        
#         if request.method == 'POST':
            
#             academic_year_name = request.POST.get('academic_year_name')
            
#             filtered_data = Result.objects.filter(academic_year=academic_year_name)
          
        
#             if not filtered_data.exists():
               
#                 extra_context["error_message"] = "No data found for the selected academic year." 
#                 return super().changelist_view(request, extra_context=extra_context)

           
#             pdf = self.generate_pdf(filtered_data,logo_url,academic_year_name)
            
          
#             response = HttpResponse(pdf, content_type='application/pdf')
#             response['Content-Disposition'] = 'attachment; filename="annual_report.pdf"'
#             return response

#         return super().changelist_view(request, extra_context=extra_context)

#     def generate_pdf(self, filtered_data, logo_url,academic_year_name): 

#         html_content = render_to_string('admin/report_annual_.html', {'data': filtered_data,'logo_url': logo_url,'academic_year': academic_year_name})
#         pdf = weasyprint.HTML(string=html_content).write_pdf()
#         return pdf
    
    

#     def has_add_permission(self, request):
#         return False
    
    
