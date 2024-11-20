from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect
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


from django.shortcuts import render, get_object_or_404
from admission.models import StudentRegistration

def add_assessment(request, registration_number):
   
    registration_number = request.session.get('registration_number')
    
    if registration_number:
       student = StudentRegistration.objects.filter(registration_number=registration_number).first()
       if student:
           subjects = student.subjects.all()
       else:
           subjects = []

    
    

    # Pass the student details to the template
    return render(request, 'admin/add_assessment.html', {
        'student': student,
        'subjects': subjects,
    })


from django.shortcuts import render, redirect
from django.http import JsonResponse
from main_setting.models import Subject
from Record_results.models import QueResults, StudentsResult


def save_assessment(request):
    if request.method == 'POST':
        registration_number = request.POST.get('registration_number')
        entry_year = request.POST.get('entry_year')
        entry_term = request.POST.get('entry_term')
        entry_programme = request.POST.get('entry_programme')
        entry_class = request.POST.get('entry_class')
        stream_name = request.POST.get('stream_name')

        # Loop through the submitted subjects
        for key, value in request.POST.items():
            if key.startswith('mt3_'):
                subject_id = key.split('_')[1]  # Extract subject ID
                try:
                    subject = Subject.objects.get(id=subject_id)
                    # Save data to StudentAssessment
                    StudentsResult.objects.create(
                        registration_number=registration_number,
                        entry_year=entry_year,
                        entry_term=entry_term,
                        entry_programme=entry_programme,
                        entry_class=entry_class,
                        stream_name=stream_name,
                        subject=subject,
                        full_name=request.POST.get('full_name'),
                        mt3=request.POST.get(f'mt3_{subject_id}'),
                        mt4=request.POST.get(f'mt4_{subject_id}'),
                        mte2=request.POST.get(f'mte2_{subject_id}'),
                        ae=request.POST.get(f'ae_{subject_id}'),
                        hpbt1=request.POST.get(f'hpbt1_{subject_id}'),
                        hpbt2=request.POST.get(f'hpbt2_{subject_id}'),
                        hpbt3=request.POST.get(f'hpbt3_{subject_id}'),
                        average=request.POST.get(f'average_{subject_id}'),
                        grade=request.POST.get(f'grade_{subject_id}'),
                        remark=request.POST.get(f'remark_{subject_id}'),
                        position=request.POST.get(f'position_{subject_id}')
                    )
                except Subject.DoesNotExist:
                    continue  # Skip subjects that don't exist

        messages.success(request, "Results added successfully!")
        return redirect('admin:index')  # Redirect to the admin homepage 

    return JsonResponse({'error': 'Invalid request'}, status=400)
