from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.utils import timezone

from admission.models import StudentRegistration
from Record_results.models import StudentAssessments, StudentsResult, StudentsResult

def generate_report(request, student_id):
    student = StudentRegistration.objects.get(pk=student_id)
    subjects = StudentRegistration.objects.filter(student=student)
    context = {
        'school_name': 'Kondoa Girls School',
        'report_title': 'Student Performance Report',
        'generation_date': timezone.now().strftime('%Y-%m-%d'),
        'student': student,
        'subjects': subjects,
        'prepared_by': 'Admin',
    }
    return render(request, 'report_template.html', context)


from django.http import HttpResponse
from weasyprint import HTML


def generate_pdf_report(request, student_id):
    student = StudentRegistration.objects.get(pk=student_id)
    subjects = StudentRegistration.objects.filter(student=student)
    context = {
        'school_name': 'Kondoa Girls School',
        'report_title': 'Student Performance Report',
        'generation_date': timezone.now().strftime('%Y-%m-%d'),
        'student': student,
        'subjects': subjects,
        'prepared_by': 'Admin',
    }
    html_content = render_to_string('report_template.html', context)
    pdf_file = HTML(string=html_content).write_pdf()
    response = HttpResponse(pdf_file, content_type='application/pdf')
    response['Content-Disposition'] = f'inline; filename="{student.full_name}_report.pdf"'
    return response


from django.http import HttpResponse
from django.template.loader import render_to_string
from weasyprint import HTML
from django.contrib.staticfiles.storage import staticfiles_storage
from django.templatetags.static import static
from django.db.models import Avg
from django.db.models import Avg, Count, Q

def download_assessment(request, registration_number, academic_year, term):
    logo_url = request.build_absolute_uri(static('logo_.png'))
    date = timezone.now().strftime('%d-%m-%Y')
    profile_image = request.build_absolute_uri(static('profile.png'))
    
    student = StudentRegistration.objects.filter(registration_number=registration_number).first()
    
    student_results = StudentsResult.objects.filter(
        registration_number=registration_number,
        # entry_year=academic_year,
        entry_term=term
    )
    
    total_average = StudentsResult.objects.filter(
     registration_number=registration_number,
     entry_term=term
    ).aggregate(total_avg=Avg('average'))['total_avg']
    
    higher_avg_count = StudentsResult.objects.filter(average__gt=total_average).count()

    row_count = StudentsResult.objects.filter(
        registration_number=registration_number,entry_term=term).count()
    
    
    higher_avg_count2 = StudentsResult.objects.filter(
        registration_number=registration_number,
        entry_term=term, average__gt=higher_avg_count).count()
    
    position = higher_avg_count2 + 1
    
    total_rows = StudentsResult.objects.count()


    if row_count > 0:
       total_avg_per_row = total_average / row_count
      
   

    
    student_assessments = StudentAssessments.objects.filter(
        registration_number=registration_number,
        # entry_year=academic_year,
        entry_term=term
    )
    
    
    student_info = student
    student_details = {
            
            'name': f"{student_info.first_name} {student_info.last_name}" if student_info else "N/A",
            'registration_no': student_info.registration_number if student_info else "N/A",
            'sex': student_info.gender if student_info else "N/A",
            'birth_date': student_info.birth_date.strftime('%d-%m-%Y') if student_info.birth_date else "N/A",
            'admission_date': student_info.admission_date.strftime('%d-%m-%Y') if student_info.admission_date else "N/A",
            'programme': student_info.stream_name if student_info.stream_name else "N/A",
            'class_name': student_info.entry_class if student_info else "N/A"
        }
    
 
    context = {

        'student_details': student_details,  
        'student_academic_info':student_results,
        'student_assessments':student_assessments,
        'logo_url': logo_url,
        'profile_image': profile_image,
        'date': date,
        'academic_year': academic_year,
        'term': term,
        'total_average': total_average,
        'average': total_avg_per_row,
        'position':position,
        'outOff':total_rows
    }
    

    
  
    html_string = render_to_string('admin/students_details.html', context)
    pdf = HTML(string=html_string).write_pdf()
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="Student_progress_report.pdf"'
    return response


