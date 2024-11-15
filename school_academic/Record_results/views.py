from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect
from Record_results.models import QueResults
from django.shortcuts import redirect
from django.contrib import messages
from django.db.models import Max
from exam_setting.models import GradeScale
from reports.models import StudentAssessment


def add_results_view(request):
    if request.method == 'POST':
        # Get the selected criteria from the form
        academic_year = request.POST.get('selected_academic_year')
        term = request.POST.get('selected_term')
        programme = request.POST.get('selected_programme')
        selected_class = request.POST.get('selected_class')
        subject = request.POST.get('selected_subject')
        exam_type = request.POST.get('selected_exams')
        
       
        
     
        # Process each selected student
        selected_students = request.POST.getlist('selected_students')
        for student_id in selected_students:
            registration_number = request.POST.get(f'student_registration_number_{student_id}')
            first_name = request.POST.get(f'student_first_name_{student_id}')
            last_name = request.POST.get(f'student_last_name_{student_id}')
            subject_result = request.POST.get(f'result_{student_id}')
            
            # Insert into QueResults model
            QueResults.objects.create(
                academic_year=academic_year,
                term=term,
                programme=programme,
                class_name=selected_class,
                # stream=stream_name,
                registration_number=registration_number,
                student_name = f'{first_name} {last_name}',
                exam_type=exam_type,
                subject=subject,
                result=subject_result,
                result_summary = f'{subject}={subject_result}',
                
            )

        messages.success(request, "Results added successfully!")
        return redirect('admin:index')  # Redirect to the admin homepage 


from django.shortcuts import redirect
from django.contrib import messages

def add_assessments_view(request):
    if request.method == 'POST':
        # Extracting form data
        academic_year = request.POST.get('selected_academic_year')
        term = request.POST.get('selected_term')
        programme = request.POST.get('selected_programme')
        selected_class = request.POST.get('selected_class')
        student_reg = request.POST.get('student_registration_number')
        student_fname = request.POST.get('student_first_name')
        student_lname = request.POST.get('student_last_name')
        assessment_grade = request.POST.get('assessment_grade')

     

        # Saving the assessment record
        StudentAssessment.objects.create(
           academic_year=academic_year if academic_year else None,
           term=term if term else None,
           programme=programme if programme else None,
           student_class=selected_class if selected_class else None,
           registration_number=student_reg if student_reg else None,
           first_name=student_fname if student_fname else None,
           last_name=student_lname if student_lname else None,
           assessment_grade=assessment_grade if assessment_grade else None,
           )


        # Success message and redirection
        messages.success(request, "Student Assessment added successfully!")
        return redirect('admin:index')  # Redirect to the admin homepage

    # If not a POST request, redirect to the admin homepage
    return redirect('admin:index')



# views.py

from django.shortcuts import render

def success_page(request):
    return render(request, 'success_page.html')
