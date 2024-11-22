from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect
from django.shortcuts import redirect
from django.contrib import messages
from django.db.models import Max
from exam_setting.models import ExamsCategory, GradeDivision, GradeScale
from reports.models import StudentAssessment
from results.models import Result




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




from django.shortcuts import render, get_object_or_404
from admission.models import StudentRegistration

def add_assessment2(request, registration_number,extra_context=None):
    registration_number = request.session.get('registration_number')
    
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

    
    if registration_number:
       student = StudentRegistration.objects.filter(registration_number=registration_number).first()
     
       if student:
           subjects = student.subjects.all()
       else:
           subjects = []

    # Pass the student details to the template
    return render(request, 'admin/add_assessment2.html', {
        'student': student,
        'subjects': subjects,
        'extra_context': extra_context,
    })
















from django.shortcuts import render, redirect
from django.http import JsonResponse
from main_setting.models import AcademicYear, Assessment, Class, Programme, Stream, Subject, Term
from Record_results.models import QueResults, StudentsResult
from collections import defaultdict

from collections import defaultdict
from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import redirect
from django.db import transaction
from django.shortcuts import redirect
from django.http import JsonResponse
from django.contrib import messages

from django.db import transaction
from django.shortcuts import redirect
from django.http import JsonResponse
from django.contrib import messages
from collections import defaultdict

from django.db import transaction
from django.shortcuts import redirect
from django.http import JsonResponse
from django.contrib import messages
from collections import defaultdict

def save_assessment(request):
    if request.method == 'POST':
        registration_number = request.POST.get('registration_number')
        entry_year = request.POST.get('entry_year')
        entry_term = request.POST.get('entry_term')
        full_name = request.POST.get('full_name')

        try:
            with transaction.atomic():
                for key, value in request.POST.items():
                    
                    if key.startswith(('mt3_', 'mt4_', 'mte2_', 'ae_', 'hpbt1_', 'hpbt2_', 'hpbt3_')):
                        subject_id = key.split('_')[1]

                        try:
                            subject = Subject.objects.get(id=subject_id)
                        except Subject.DoesNotExist:
                            continue

                        subject_name = request.POST.get(f'subject_name_{subject_id}')
                        mt3 = float(request.POST.get(f'mt3_{subject_id}', 0) or 0)
                        mt4 = float(request.POST.get(f'mt4_{subject_id}', 0) or 0)
                        mte2 = float(request.POST.get(f'mte2_{subject_id}', 0) or 0)
                        ae = float(request.POST.get(f'ae_{subject_id}', 0) or 0)
                        hpbt1 = float(request.POST.get(f'hpbt1_{subject_id}', 0) or 0)
                        hpbt2 = float(request.POST.get(f'hpbt2_{subject_id}', 0) or 0)
                        hpbt3 = float(request.POST.get(f'hpbt3_{subject_id}', 0) or 0)
                        
                        total = 0
                        average = 0
                   
                        values = [mt3, mt4, mte2, ae, hpbt1, hpbt2, hpbt3]
                        valid_values = [value for value in values if value not in (None, 0)]
                        if valid_values:
                           total = sum(valid_values)
                           average = total / len(valid_values)
                      
                        if 80 <= average <= 100:
                            grade = 'A'
                            remark = 'Excellent'
                        elif 70 <= average < 79:
                            grade = 'B' 
                            remark = 'Very good'    
                        elif 60 <= average < 69:
                            grade = 'C'
                            remark = 'Good'  
                        elif 50 <= average < 59:
                            grade = 'D'
                            remark = 'Average'
                            
                        elif 40 <= average < 49:
                            grade = 'D'
                            remark = 'Satisfactory'  
                        else:
                            grade = 'F'
                            remark = 'Fail' 

                        result_que, created = StudentsResult.objects.get_or_create(
                           
                            subject_name=subject_name,
                        )
                        if (
                            
                            result_que.mt3 != mt3 or 
                            result_que.mt4 != mt4 or 
                            result_que.mte2 != mte2 or 
                            result_que.ae != ae or 
                            result_que.hpbt1 != hpbt1 or 
                            result_que.hpbt2 != hpbt2 or 
                            result_que.hpbt3 != hpbt3 or 
                            result_que.average != average or 
                            result_que.grade != grade or 
                            result_que.remark != remark or 
                            result_que.full_name != full_name
                        ):
                            result_que.mt3 = mt3
                            result_que.mt4 = mt4
                            result_que.mte2 = mte2
                            result_que.ae = ae
                            result_que.hpbt1 = hpbt1
                            result_que.hpbt2 = hpbt2
                            result_que.hpbt3 = hpbt3
                            result_que.average = average
                            result_que.grade = grade
                            result_que.remark = remark
                            result_que.full_name = full_name
                        result_que.save()
                        
                        
                        

                        # Update position for this subject only
                        position = StudentsResult.objects.filter(
                            subject_name=subject_name,
                            average__gt=average
                        ).count() + 1
                        result_que.position = position
                        result_que.save()

                        # Update specific fields in `Result`
                        Result.objects.update_or_create(
                            academic_year=entry_year,
                            term=entry_term,
                            registration_number=registration_number,
                            subject=subject_name,
                            defaults={
                                'total': total,
                                'avg': average,
                                'grade': grade,
                                # 'division': division_title
                            }
                        )

            messages.success(request, "Results processed successfully!")
            return redirect('admin:index')

        except Exception as e:
            messages.error(request, f"An error occurred: {str(e)}")
            return redirect('admin:index')

    return JsonResponse({'error': 'Invalid request'}, status=400)





from django.shortcuts import render, redirect
from django.http import JsonResponse
from main_setting.models import AcademicYear, Assessment, Class, Programme, Stream, Subject, Term
from Record_results.models import QueResults, StudentsResult

from django.shortcuts import redirect
from django.http import JsonResponse
from django.contrib import messages
from .models import StudentAssessments, StudentRegistration, StudentsResult


def save_assessment2(request):
    if request.method == "POST":
        # Extract basic student info from hidden fields
        registration_number = request.POST.get("registration_number")
        full_name = request.POST.get("full_name")
        entry_year = request.POST.get("entry_year")
        entry_term = request.POST.get("entry_term")
        entry_programme = request.POST.get("entry_programme")
        entry_class = request.POST.get("entry_class")
        stream_name = request.POST.get("stream_name")

        # Iterate over assessments and either update or insert
        for key, value in request.POST.items():
            if key.startswith("grade_"):  # Check for grade fields
                # Extract assessment ID from the key
                assessment_id = key.split("_")[1]
                subject_name = request.POST.get(f"subject_name_{assessment_id}")
                grade = value

                # Check if a record with the same details exists
                assessment, created = StudentAssessments.objects.update_or_create(
                    registration_number=registration_number,
                    full_name=full_name,
                    entry_year=entry_year,
                    entry_term=entry_term,
                    assessment_name=subject_name,
                    defaults={
                        "entry_programme": entry_programme,
                        "entry_class": entry_class,
                        "stream_name": stream_name,
                        "grade": grade,
                    },
                )

                # Log the action (optional, for debugging)
                if created:
                    print(f"Created new assessment: {assessment}")
                else:
                    print(f"Updated existing assessment: {assessment}")

        # Success message
        messages.success(request, "Students Assessments added successfully!")
        return redirect('admin:index')  # Redirect to the admin homepage

    return JsonResponse({'error': 'Invalid request'}, status=400)


