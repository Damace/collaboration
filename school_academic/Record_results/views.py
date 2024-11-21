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
                    subject_code = request.POST.get(f'subject_code_{subject_id}')
                    subject_name = request.POST.get(f'subject_name_{subject_id}')

                    # Retrieve marks
                    mt3 = float(request.POST.get(f'mt3_{subject_id}', 0) or 0)
                    mt4 = float(request.POST.get(f'mt4_{subject_id}', 0) or 0)
                    mte2 = float(request.POST.get(f'mte2_{subject_id}', 0) or 0)
                    ae = float(request.POST.get(f'ae_{subject_id}', 0) or 0)
                    hpbt1 = float(request.POST.get(f'hpbt1_{subject_id}', 0) or 0)
                    hpbt2 = float(request.POST.get(f'hpbt2_{subject_id}', 0) or 0)
                    hpbt3 = float(request.POST.get(f'hpbt3_{subject_id}', 0) or 0)

                    # Calculate average only for the current subject
                    average = (mt3 + mt4 + mte2 + ae + hpbt1 + hpbt2 + hpbt3) / 7

                    # Determine grade and remark
                    if average >= 90:
                        grade = 'A'
                        remark = 'EXCELLENT'
                    elif average >= 80:
                        grade = 'B'
                        remark = 'VERY GOOD'
                    elif average >= 70:
                        grade = 'C'
                        remark = 'GOOD'
                    elif average >= 60:
                        grade = 'D'
                        remark = 'FAIR'
                    elif average >= 50:
                        grade = 'E'
                        remark = 'PASS'
                    elif average >= 40:
                        grade = 'F'
                        remark = 'FAIL'
                    else:
                        grade = '0'
                        remark = 'POOR'

                    # Check if the record already exists
                    existing_result = StudentsResult.objects.filter(
                        registration_number=registration_number,
                        entry_year=entry_year,
                        entry_term=entry_term,
                        subject_code=subject_code,
                        subject_name=subject_name
                    ).first()

                    if existing_result:
                        # Update only the score fields that are provided in the POST request
                        if request.POST.get('full_name'):
                            existing_result.full_name = request.POST.get('full_name')

                        # Update marks only if provided
                        existing_result.mt3 = mt3 if request.POST.get(f'mt3_{subject_id}') else existing_result.mt3
                        existing_result.mt4 = mt4 if request.POST.get(f'mt4_{subject_id}') else existing_result.mt4
                        existing_result.mte2 = mte2 if request.POST.get(f'mte2_{subject_id}') else existing_result.mte2
                        existing_result.ae = ae if request.POST.get(f'ae_{subject_id}') else existing_result.ae
                        existing_result.hpbt1 = hpbt1 if request.POST.get(f'hpbt1_{subject_id}') else existing_result.hpbt1
                        existing_result.hpbt2 = hpbt2 if request.POST.get(f'hpbt2_{subject_id}') else existing_result.hpbt2
                        existing_result.hpbt3 = hpbt3 if request.POST.get(f'hpbt3_{subject_id}') else existing_result.hpbt3

                        # Only update the average, grade, and remark if scores have changed
                        if any([
                            existing_result.mt3 != mt3,
                            existing_result.mt4 != mt4,
                            existing_result.mte2 != mte2,
                            existing_result.ae != ae,
                            existing_result.hpbt1 != hpbt1,
                            existing_result.hpbt2 != hpbt2,
                            existing_result.hpbt3 != hpbt3
                        ]):
                            existing_result.average = average
                            existing_result.grade = grade
                            existing_result.remark = remark
                            # Calculate position based on the current subject's scores
                            position = StudentsResult.objects.filter(
                                subject_code=subject_code,
                                subject_name=subject_name,
                                average__gt=average
                            ).count() + 1  # Position is 1 plus the count of students with higher averages
                            existing_result.position = position

                        existing_result.save()  # Save the updated record

                    else:
                        # Create new record if it doesn't exist
                        StudentsResult.objects.create(
                            registration_number=registration_number,
                            entry_year=entry_year,
                            entry_term=entry_term,
                            entry_programme=entry_programme,
                            entry_class=entry_class,
                            stream_name=stream_name,
                            subject_code=subject_code,
                            subject_name=subject_name,
                            full_name=request.POST.get('full_name'),
                            mt3=mt3,
                            mt4=mt4,
                            mte2=mte2,
                            ae=ae,
                            hpbt1=hpbt1,
                            hpbt2=hpbt2,
                            hpbt3=hpbt3,
                            average=average,
                            grade=grade,
                            remark=remark,
                        )

                except Subject.DoesNotExist:
                    continue 

        messages.success(request, "Results processed successfully!")
        return redirect('admin:index')  # Redirect to the admin homepage
    # Redirect to the admin homepage  # Redirect to the admin homepage # Redirect to the admin homepage # Redirect to the admin homepage
    return JsonResponse({'error': 'Invalid request'}, status=400)
