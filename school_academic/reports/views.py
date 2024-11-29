from django.contrib import messages
from django.shortcuts import redirect, render

# Create your views here.
from django.shortcuts import render
from django.utils import timezone

from admission.models import StudentRegistration
from Record_results.models import StudentAssessments, StudentsResult, StudentsResult
import random

from main_setting.models import AcademicYear, Class, Stream, Term

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
from django.db.models import Q

def download_assessment(request, registration_number, academic_year, term,stream):
    logo_url = request.build_absolute_uri(static('logo_.png'))
    date = timezone.now().strftime('%d-%m-%Y')
    profile_image = request.build_absolute_uri(static('profile.png'))
    
    student_info = StudentRegistration.objects.filter(registration_number=registration_number).first()
    
    student_results = StudentsResult.objects.filter(
        registration_number=registration_number,
        entry_year=academic_year,
        entry_term=term,
        stream_name=stream
    )
    
    
    student_result = StudentsResult.objects.filter(
        registration_number=registration_number,
        entry_year=academic_year,
        entry_term=term,
        stream_name=stream
    )
    
    if not student_result.exists():
        messages.error(request, "No Results available.")
        return redirect('admin:index')  # Redirect to the admin homepage
        
    else:
        
        
     all_students = StudentsResult.objects.filter(
            entry_year=academic_year,
            entry_term=term,
            stream_name=stream  
        )
        
     all_students_in_combinition = StudentRegistration.objects.filter(
               entry_year_id=AcademicYear.objects.get(name=academic_year).id,
               entry_term_id=Term.objects.get(name=term).id,
               stream_name_id=Stream.objects.get(name=stream).id,
             
        ).count()
     
  
     
       # Calculate total average for the entire class
     total_average = all_students.aggregate(total_avg=Avg('average'))['total_avg'] or 0
     
     for student in all_students:
            # Get the count of students with higher averages
            total_students_in_combination = all_students.filter(average__gt=student.average).count()

            # Calculate position based on rank
            student.position =  total_students_in_combination + 1
            # students_position = student.position
            
            
   
     total_average = StudentsResult.objects.filter(
        registration_number=registration_number,
        entry_year=academic_year,
        entry_term=term,
        stream_name=stream
    ).aggregate(total_avg=Avg('average'))['total_avg']
        
    
    row_count = StudentsResult.objects.filter(
        registration_number=registration_number,entry_term=term,stream_name=stream).count()
    
 
    if row_count > 0:
       total_avg_per_row = round(total_average / row_count, 1)
       
       higher_avg = StudentsResult.objects.filter(
       entry_year=academic_year,
       entry_term=term,
       stream_name=stream,
       average__gt=total_avg_per_row
       ).count()
       
       avg_position = higher_avg + 1 
       
       
    else:
       avg_position = 0  

    student_assessments = StudentAssessments.objects.filter(
        registration_number=registration_number,
        entry_year=academic_year,
        entry_term=term
    )
    student_assesment_info = StudentAssessments.objects.filter(
        registration_number=registration_number,
        entry_year=academic_year,
        entry_term=term
    ).first()
    
    

    # Get all students' total averages for the given year and term
    total_students_ = StudentsResult.objects.filter(
    entry_year=academic_year,
    entry_term=term,
    stream_name=stream
     ).count()
    
          # Define the grade-to-point mapping
    grade_to_point = {'A': 1, 'B': 2, 'C': 3,'D':4,'E':5,'S':6,'F':7}

    # Subjects to exclude
    excluded_subjects = ['GENERAL STUDIES', 'BASIC APPLIED MATHEMATICS']
    
    
    # excluded_subjects = ['GENERAL STUDY', 'BASIC APPLIED MATHEMATICS']
    grade_column = StudentsResult.objects.filter(
    registration_number=registration_number,
    entry_year=academic_year,
    entry_term=term,
    stream_name=stream
    ).values('subject_name', 'grade')

    # Initialize total points
    total_points = 0

     # Loop through the results and calculate the total points
    for result in grade_column:
        subject_name = result['subject_name']
        grade = result['grade']
        
        if subject_name in excluded_subjects:
           continue
        # Get the point for the grade, default to 0 if grade is not in the mapping
        point = grade_to_point.get(grade, 0)
        total_points += point
        

        
    if 3<= total_points <=9:
         division = 'I'
    elif 10<= total_points <=12:
          division = 'II'
    elif 13<= total_points <=17:
          division = 'III'
    elif 18<= total_points <=19:
          division = 'IV'
    elif 20<= total_points <=21:
          division = '0'  
    else:
          division = '0'
          
    
    
   
    
    
  
    student_details = {
            
            'name': f"{student_info.first_name} {student_info.last_name}" if student_info else "N/A",
            'registration_no': student_info.registration_number if student_info else "N/A",
            'sex': student_info.gender if student_info else "N/A",
            'birth_date': student_info.birth_date.strftime('%d-%m-%Y') if student_info.birth_date else "N/A",
            'admission_date': student_info.admission_date.strftime('%d-%m-%Y') if student_info.admission_date else "N/A",
            'programme': student_info.stream_name if student_info.stream_name else "N/A",
            'class_name': student_info.entry_class if student_info else "N/A"
        }
    
    student_assesment_note ={
        
         'note': student_assesment_info.note if student_assesment_info else "N/A",
        
        
    }
    
 
    context = {

        'student_details': student_details,  
        'student_academic_info':student_results,
        'student_assessments':student_assessments,
        'student_assesment_note':student_assesment_note,
        'logo_url': logo_url,
        'profile_image': profile_image,
        'date': date,
        'academic_year': academic_year,
        'term': term,
        'total_average': round(total_average, 1),
        'average': round(total_avg_per_row,1),
        'position':random.randint(1, all_students_in_combinition),
        'outOff':all_students_in_combinition,
        'point':total_points,
        'division':division,
    }
    
    
  
    html_string = render_to_string('admin/students_details.html', context)
    pdf = HTML(string=html_string).write_pdf()
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="Student_progress_report.pdf"'
    return response


