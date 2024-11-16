from django.contrib import admin

from .models import StudentProxy, StudentRegistration


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
from django.utils.html import format_html


@admin.register(StudentProxy)
class StudentProxyAdmin(admin.ModelAdmin):
    
    
    change_list_template = "admin/myditails_students.html"
    
    def logged_user(self, request):
        """
        Displays details of the logged-in user in the admin interface.
        """
        user = request.user
        
        print('dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd',user)
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
            academic_year = request.POST.get("academic_year")
            term = request.POST.get("term")
            
            
   
            filtered_students2 = StudentRegistration.objects.filter(registration_number=reg_number
             )
            filtered_students = Result.objects.filter(
                academic_year=academic_year,
                registration_number=reg_number,
                term=term,
                )
            
            if not filtered_students.exists():
                extra_context["error_message"] = "No Students with Registration Number, selected Academic year and term."
                return super().changelist_view(request, extra_context=extra_context)
            else:
                extra_context["filtered_students"] = filtered_students
                extra_context["filtered_students2"] = filtered_students2

            pdf = self.generate_pdf(filtered_students, filtered_students2, logo_url,academic_year,term, profile_image)


            response = HttpResponse(pdf, content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="annual_report.pdf"'
            return response

        return super().changelist_view(request, extra_context=extra_context)
        
    def generate_pdf(self, filtered_data, filtered_data_2, logo_url,academic_year,term,profile_image): 
        date = timezone.now().strftime('%d-%m-%Y')

        # Extract student details from filtered_students2
        student_info = filtered_data_2.first()  # Assuming only one student is filtered

        student_details = {
            
            'name': f"{student_info.first_name} {student_info.last_name}" if student_info else "N/A",
            'registration_no': student_info.registration_number if student_info else "N/A",
            'sex': student_info.gender if student_info else "N/A",
            'birth_date': student_info.birth_date.strftime('%d-%m-%Y') if student_info.birth_date else "N/A",
            'admission_date': student_info.admission_date.strftime('%d-%m-%Y') if student_info.admission_date else "N/A",
            'programme': student_info.entry_programme.name if student_info.entry_programme else "N/A",
            'class_name': student_info.entry_class if student_info else "N/A"
        }
        
        # Prepare results
        results = []
        total_average = 0
        total_subjects = filtered_data.count()
        
        for i, result in enumerate(filtered_data, start=1):
            results.append({
                'sn': i,
                'subject_name': result.subject,
                'total': result.total,
                'average': result.avg,
                'remark': result.point,
                'grade': result.grade,
                'position': result.division,
              
            })
            total_average += result.avg if result.avg is not None else 0

        overall_average = total_average / total_subjects if total_subjects > 0 else 0
        overall_position = filtered_data_2.first().registration_number if filtered_data_2.exists() else "N/A"

        # Render the HTML with student details and results
        html_content = render_to_string('admin/students_details.html', {
            'data': filtered_data,
            'student_details': student_details,
            'results': results,
            'overall_average': overall_average,
            'overall_position': overall_position,
            'logo_url': logo_url,
            'profile_image': profile_image,
            'date': date,
            'academic_year': academic_year,
             'term': term,
        })
        pdf = weasyprint.HTML(string=html_content).write_pdf()
        return pdf

    def has_add_permission(self, request):
        return False

