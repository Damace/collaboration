from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect
from django.shortcuts import redirect
from django.contrib import messages
from django.db.models import Max
from exam_setting.models import ExamsCategory, GradeDivision, GradeScale
from reports.models import StudentAssessment
from results.models import Result

from django.contrib import messages
from django.shortcuts import redirect
from django.db import transaction

from django.shortcuts import redirect
from django.contrib import messages
from django.db import transaction
from .models import ClassResults, StudentsResult, GradeScale
import random

def add_results_view(request):
    if request.method == 'POST':
       
        academic_year = request.POST.get('selected_academic_year')
        term = request.POST.get('selected_term')
        programme = request.POST.get('selected_programme')
        selected_stream = request.POST.get('selected_stream')
        selected_class = request.POST.get('selected_class')
        subject_code = request.POST.get('selected_subject_code')
        subject = request.POST.get('selected_subject')
        exam_type = request.POST.get('selected_exams')
        
        

        # Get selected students
        selected_students = request.POST.getlist('selected_students')
        
    
        
        try:
            with transaction.atomic():  # Ensure atomic database transactions
                for student_id in selected_students:
                    # Retrieve student-specific data
                    registration_number = request.POST.get(f'student_registration_number_{student_id}')
                    first_name = request.POST.get(f'student_first_name_{student_id}')
                    last_name = request.POST.get(f'student_last_name_{student_id}')
                    subject_result = float(request.POST.get(f'result_{student_id}','') or '')
                    
                    
                    
                    if exam_type == 'TERMINAL EXAMINATION':
                        te = subject_result
                        ane = mtt2 = mtt1 = mte =  0  
                 
                    elif exam_type == 'ANNUAL EXAMINATION':
                        ane = subject_result
                        te = mtt2 = mtt1 = mte =  0  
                    elif exam_type == 'MONTHLY TEST 2':
                        mtt2 = subject_result
                        te = ane = mtt1 = mte =  0  
                    elif exam_type == 'MONTHLY TEST 1':
                        mtt1 = subject_result
                        te = ane = mtt2 = mte =  0  
                    elif exam_type == 'MIDTERM EXAMINATION':
                        mte = subject_result
                        te = ane = mtt2 = mtt1 =  0 
                        
                    
                      
                    if 80 <= subject_result <= 100:
                            grade = 'A'
                            remark = 'Excellent'
                    elif 70 <= subject_result < 79:
                            grade = 'B' 
                            remark = 'Very good'    
                    elif 60 <= subject_result < 69:
                            grade = 'C'
                            remark = 'Good'  
                    elif 50 <= subject_result < 59:
                            grade = 'D'
                            remark = 'Average'
                            
                    elif 40 <= subject_result < 49:
                            grade = 'E'
                            remark = 'Satisfactory'  
                     
                    elif 35 <= subject_result < 39:
                            grade = 'S'
                            remark = 'Subsidiary' 
                    else:
                            grade = 'F'
                            remark = 'Fail' 

                    student_result = StudentsResult.objects.filter(
                    registration_number=registration_number,
                    entry_year=academic_year,
                    entry_term=term,
                    subject_name=subject
                    ).first()
                    
                    
                    if student_result is None:
                        
                        student_result = StudentsResult(
                        registration_number=registration_number,
                        entry_year=academic_year,
                        entry_term=term,
                        entry_programme=programme,
                        stream_name=selected_stream,
                        entry_class=selected_class,
                        subject_name=subject,
                        subject_code = subject_code,
                        te=te ,
                        ane=ane,
                        mtt2=mtt2,
                        mtt1=mtt1,
                        mte=mte,
                        average=subject_result,
                        grade=grade,
                        remark=remark,
                        full_name=f"{first_name} {last_name}",
                        result_summary=f", {subject} = {subject_result}",
                        position=random.uniform(1, 100)  # Set position to a random value
                      )
                        student_result.save() 
                        
                    else:
                        update_fields = []
                        
                   
                        
                        if te == 0:
                           te = student_result.te  
                        else:
                           student_result.te = te
                           update_fields.append('te')
                 
                        if ane == 0:
                           ane = student_result.ane  
                        else:
                           student_result.ane = ane
                           update_fields.append('ane')    
                 
                        if mtt2 == 0:
                           mtt2 = student_result.mtt2  
                        else:
                           student_result.mtt2 = mtt2
                           update_fields.append('mtt2')  
                    
                        if mtt1 == 0:
                           mtt1 = student_result.mtt1 
                        else:
                           student_result.mtt1 = mtt1
                           update_fields.append('mtt1')  
                    
                        if mte == 0:
                           mte = student_result.mte 
                        else:
                           student_result.mte = mte
                           update_fields.append('mte') 
                           
                
                        if student_result.full_name != f"{first_name} {last_name}":
                           student_result.full_name = f"{first_name} {last_name}"
                           update_fields.append('full_name')
                        if student_result.result_summary != f", {subject} = {subject_result}":
                           student_result.result_summary = f", {subject} = {subject_result}"
                           update_fields.append('result_summary')
                           
                        if update_fields:
                           student_result.position = random.uniform(1, 100)    
                           
                        if student_result:
                           te_ = float(student_result.te) 
                           ane_ = float(student_result.ane)
                           mtt1_ = float(student_result.mtt1) 
                           mtt2_ = float(student_result.mtt2) 
                           mte_ = float(student_result.mte) 
                        
                        values = [te_, ane_, mtt1_, mtt2_, mte_]
                        valid_values = [value for value in values if value != 0]  
                        if valid_values:
                           total = sum(valid_values)
                           average = total / len(valid_values)  
                           
                           
                           
                           if 80 <= average <= 100:
                              grade = 'A'
                              remark = 'Excellent'
                              if student_result.grade != grade:
                                 student_result.grade = grade
                                 update_fields.append('grade')
                              if student_result.remark != remark:
                                 student_result.remark = remark
                                 update_fields.append('remark')
                                            
                           elif 70 <= average < 79:
                              grade = 'B' 
                              remark = 'Very good'  
                              if student_result.grade != grade:
                                 student_result.grade = grade
                                 update_fields.append('grade')
                              if student_result.remark != remark:
                                 student_result.remark = remark
                                 update_fields.append('remark')  
                           elif 60 <= average < 69:
                              grade = 'C'
                              remark = 'Good'  
                              if student_result.grade != grade:
                                 student_result.grade = grade
                                 update_fields.append('grade')
                              if student_result.remark != remark:
                                 student_result.remark = remark
                                 update_fields.append('remark')
                           elif 50 <= average < 59:
                              grade = 'D'
                              remark = 'Average'
                              if student_result.grade != grade:
                                 student_result.grade = grade
                                 update_fields.append('grade')
                              if student_result.remark != remark:
                                 student_result.remark = remark
                                 update_fields.append('remark')
                            
                           elif 40 <= average < 49:
                              grade = 'E'
                              remark = 'Satisfactory'  
                              if student_result.grade != grade:
                                 student_result.grade = grade
                                 update_fields.append('grade')
                              if student_result.remark != remark:
                                 student_result.remark = remark
                                 update_fields.append('remark')
                                 
                           elif 35 <= average < 39:
                              grade = 'S'
                              remark = 'Subsidiary'  
                              if student_result.grade != grade:
                                 student_result.grade = grade
                                 update_fields.append('grade')
                              if student_result.remark != remark:
                                 student_result.remark = remark
                                 update_fields.append('remark')    
                                 
                                 
                           else:
                              grade = 'F'
                              remark = 'Fail' 
                              if student_result.grade != grade:
                                 student_result.grade = grade
                                 update_fields.append('grade')
                              if student_result.remark != remark:
                                 student_result.remark = remark
                                 update_fields.append('remark')
                           
                                  
                           
                           if student_result.average != average:
                              student_result.average = average
                              student_result.save(update_fields=['average'])
                
                           
                           student_result.save(update_fields=update_fields)    
                            
                    groups = StudentsResult.objects.values(
                        'registration_number',
                        'entry_year',
                        'entry_term',
                        'entry_programme',
                        'entry_class',
                        'stream_name',
                        'full_name',
                        'average',
                        'grade',
                        'remark',
                        'position'
                        ).distinct()
                    
                    for group in groups:
                        
                        results = StudentsResult.objects.filter(
                            registration_number=group['registration_number'],
                            entry_year=group['entry_year'],
                            entry_term=group['entry_term']
                              )

           
                        subjects = ", ".join(result.subject_name for result in results)
                        
                        valid_scores = []
                        for result in results:
                            if result.te and float(result.te) > 0:
                                valid_scores.append(str(float(result.te)))
                            if result.ane and float(result.ane) > 0:
                                valid_scores.append(str(float(result.ane)))
                            if result.mtt2 and float(result.mtt2) > 0:
                                valid_scores.append(str(float(result.mtt2)))
                            if result.mtt1 and float(result.mtt1) > 0:
                                valid_scores.append(str(float(result.mtt1)))
                            if result.mte and float(result.mte) > 0:
                                valid_scores.append(str(float(result.mte)))


                            scores = ", ".join(valid_scores)  # This is now a string, not a list
 

                       
                        # scores = ", ".join(str(result.te) for result in results)
                        
                        
                        existing_record = ClassResults.objects.filter(
                        registration_number=group['registration_number'],
                        academic_year=group['entry_year'],
                        term=group['entry_term'],
                       full_name=group['full_name'],
                       ).first()

                    if existing_record:
                        existing_record.subjects = subjects
                        existing_record.scores = scores
                        existing_record.average = group['average']
                        existing_record.grade = group['grade']
                        existing_record.remark = group['remark']
                        existing_record.position = group['position']
                        existing_record.save()

                    else:
                        ClassResults.objects.create(
                        registration_number=group['registration_number'],
                        academic_year=group['entry_year'],
                        term=group['entry_term'],
                        entry_programme=group['entry_programme'],
                        entry_class=group['entry_class'],
                        stream_name=group['stream_name'],
                        full_name=group['full_name'],
                        subjects=subjects,
                        scores=scores,
                        average=group['average'],
                        grade=group['grade'],
                       remark=group['remark'],
                       position=group['position']
                )
                        
                        
                        
                   
            messages.success(request, "Results added successfully!")
            return redirect('admin:index')  # Redirect to the admin homepage

        except Exception as e:
            messages.error(request, f"Error adding results: {str(e)}")
            return redirect('admin:index')  # Redirect back to the results form

    else:
        messages.error(request, "Invalid request method.")
        return redirect('admin:index')  # Redirect back if not POST




def edit_results_view(request):
    if request.method == 'POST':
       
        academic_year = request.POST.get('selected_academic_year')
        term = request.POST.get('selected_term')
        programme = request.POST.get('selected_programme')
        selected_stream = request.POST.get('selected_stream')
        selected_class = request.POST.get('selected_class')
        subject_code = request.POST.get('selected_subject_code')
        subject = request.POST.get('selected_subject')
        exam_type = request.POST.get('selected_exams')
        
        

        # Get selected students
        selected_students = request.POST.getlist('selected_students')
        
    
        
        try:
            with transaction.atomic():  # Ensure atomic database transactions
                for student_id in selected_students:
                    # Retrieve student-specific data
                    registration_number = request.POST.get(f'student_registration_number_{student_id}')
                    first_name = request.POST.get(f'student_first_name_{student_id}')
                    subject_result = float(request.POST.get(f'result_{student_id}','') or '')
                    
                    
                    
                    if exam_type == 'TERMINAL EXAMINATION':
                        te = subject_result
                        ane = mtt2 = mtt1 = mte =  0  
                 
                    elif exam_type == 'ANNUAL EXAMINATION':
                        ane = subject_result
                        te = mtt2 = mtt1 = mte =  0  
                    elif exam_type == 'MONTHLY TEST 2':
                        mtt2 = subject_result
                        te = ane = mtt1 = mte =  0  
                    elif exam_type == 'MONTHLY TEST 1':
                        mtt1 = subject_result
                        te = ane = mtt2 = mte =  0  
                    elif exam_type == 'MIDTERM EXAMINATION':
                        mte = subject_result
                        te = ane = mtt2 = mtt1 =  0 
                        
                    
                      
                    if 80 <= subject_result <= 100:
                            grade = 'A'
                            remark = 'Excellent'
                    elif 70 <= subject_result < 79:
                            grade = 'B' 
                            remark = 'Very good'    
                    elif 60 <= subject_result < 69:
                            grade = 'C'
                            remark = 'Good'  
                    elif 50 <= subject_result < 59:
                            grade = 'D'
                            remark = 'Average'
                            
                    elif 40 <= subject_result < 49:
                            grade = 'E'
                            remark = 'Satisfactory'  
                     
                    elif 35 <= subject_result < 39:
                            grade = 'S'
                            remark = 'Subsidiary' 
                    else:
                            grade = 'F'
                            remark = 'Fail' 

                    student_result = StudentsResult.objects.filter(
                    registration_number=registration_number,
                    entry_year=academic_year,
                    entry_term=term,
                    subject_name=subject
                    ).first()
                    
                    
                    if student_result is None:
                        
                        student_result = StudentsResult(
                        registration_number=registration_number,
                        entry_year=academic_year,
                        entry_term=term,
                        entry_programme=programme,
                        stream_name=selected_stream,
                        entry_class=selected_class,
                        subject_name=subject,
                        subject_code = subject_code,
                        te=te ,
                        ane=ane,
                        mtt2=mtt2,
                        mtt1=mtt1,
                        mte=mte,
                        average=subject_result,
                        grade=grade,
                        remark=remark,
                        full_name=first_name,
                        result_summary=f", {subject} = {subject_result}",
                        position=random.uniform(1, 100)  # Set position to a random value
                      )
                        student_result.save() 
                        
                    else:
                        update_fields = []
                        
                   
                        
                        if te == 0:
                           te = student_result.te  
                        else:
                           student_result.te = te
                           update_fields.append('te')
                 
                        if ane == 0:
                           ane = student_result.ane  
                        else:
                           student_result.ane = ane
                           update_fields.append('ane')    
                 
                        if mtt2 == 0:
                           mtt2 = student_result.mtt2  
                        else:
                           student_result.mtt2 = mtt2
                           update_fields.append('mtt2')  
                    
                        if mtt1 == 0:
                           mtt1 = student_result.mtt1 
                        else:
                           student_result.mtt1 = mtt1
                           update_fields.append('mtt1')  
                    
                        if mte == 0:
                           mte = student_result.mte 
                        else:
                           student_result.mte = mte
                           update_fields.append('mte') 
                           
                
                        if student_result.full_name != first_name:
                           student_result.full_name = first_name
                           update_fields.append('full_name')
                        if student_result.result_summary != f", {subject} = {subject_result}":
                           student_result.result_summary = f", {subject} = {subject_result}"
                           update_fields.append('result_summary')
                           
                        if update_fields:
                           student_result.position = random.uniform(1, 100)    
                           
                        if student_result:
                           te_ = float(student_result.te) 
                           ane_ = float(student_result.ane)
                           mtt1_ = float(student_result.mtt1) 
                           mtt2_ = float(student_result.mtt2) 
                           mte_ = float(student_result.mte) 
                        
                        values = [te_, ane_, mtt1_, mtt2_, mte_]
                        valid_values = [value for value in values if value != 0]  
                        if valid_values:
                           total = sum(valid_values)
                           average = total / len(valid_values)  
                           
                           
                           
                           if 80 <= average <= 100:
                              grade = 'A'
                              remark = 'Excellent'
                              if student_result.grade != grade:
                                 student_result.grade = grade
                                 update_fields.append('grade')
                              if student_result.remark != remark:
                                 student_result.remark = remark
                                 update_fields.append('remark')
                                            
                           elif 70 <= average < 79:
                              grade = 'B' 
                              remark = 'Very good'  
                              if student_result.grade != grade:
                                 student_result.grade = grade
                                 update_fields.append('grade')
                              if student_result.remark != remark:
                                 student_result.remark = remark
                                 update_fields.append('remark')  
                           elif 60 <= average < 69:
                              grade = 'C'
                              remark = 'Good'  
                              if student_result.grade != grade:
                                 student_result.grade = grade
                                 update_fields.append('grade')
                              if student_result.remark != remark:
                                 student_result.remark = remark
                                 update_fields.append('remark')
                           elif 50 <= average < 59:
                              grade = 'D'
                              remark = 'Average'
                              if student_result.grade != grade:
                                 student_result.grade = grade
                                 update_fields.append('grade')
                              if student_result.remark != remark:
                                 student_result.remark = remark
                                 update_fields.append('remark')
                            
                           elif 40 <= average < 49:
                              grade = 'E'
                              remark = 'Satisfactory'  
                              if student_result.grade != grade:
                                 student_result.grade = grade
                                 update_fields.append('grade')
                              if student_result.remark != remark:
                                 student_result.remark = remark
                                 update_fields.append('remark')
                                 
                           elif 35 <= average < 39:
                              grade = 'S'
                              remark = 'Subsidiary'  
                              if student_result.grade != grade:
                                 student_result.grade = grade
                                 update_fields.append('grade')
                              if student_result.remark != remark:
                                 student_result.remark = remark
                                 update_fields.append('remark')    
                                 
                                 
                           else:
                              grade = 'F'
                              remark = 'Fail' 
                              if student_result.grade != grade:
                                 student_result.grade = grade
                                 update_fields.append('grade')
                              if student_result.remark != remark:
                                 student_result.remark = remark
                                 update_fields.append('remark')
                           
                                  
                           
                           if student_result.average != average:
                              student_result.average = average
                              student_result.save(update_fields=['average'])
                
                           
                           student_result.save(update_fields=update_fields)    
                            
                    groups = StudentsResult.objects.values(
                        'registration_number',
                        'entry_year',
                        'entry_term',
                        'entry_programme',
                        'entry_class',
                        'stream_name',
                        'full_name',
                        'average',
                        'grade',
                        'remark',
                        'position'
                        ).distinct()
                    
                    for group in groups:
                        
                        results = StudentsResult.objects.filter(
                            registration_number=group['registration_number'],
                            entry_year=group['entry_year'],
                            entry_term=group['entry_term']
                              )

           
                        subjects = ", ".join(result.subject_name for result in results)
                        
                        valid_scores = []
                        for result in results:
                            if result.te and float(result.te) > 0:
                                valid_scores.append(str(float(result.te)))
                            if result.ane and float(result.ane) > 0:
                                valid_scores.append(str(float(result.ane)))
                            if result.mtt2 and float(result.mtt2) > 0:
                                valid_scores.append(str(float(result.mtt2)))
                            if result.mtt1 and float(result.mtt1) > 0:
                                valid_scores.append(str(float(result.mtt1)))
                            if result.mte and float(result.mte) > 0:
                                valid_scores.append(str(float(result.mte)))


                            scores = ", ".join(valid_scores)  # This is now a string, not a list
 

                       
                        # scores = ", ".join(str(result.te) for result in results)
                        
                        
                        existing_record = ClassResults.objects.filter(
                        registration_number=group['registration_number'],
                        academic_year=group['entry_year'],
                        term=group['entry_term'],
                       full_name=group['full_name'],
                       ).first()

                    if existing_record:
                        existing_record.subjects = subjects
                        existing_record.scores = scores
                        existing_record.average = group['average']
                        existing_record.grade = group['grade']
                        existing_record.remark = group['remark']
                        existing_record.position = group['position']
                        existing_record.save()

                    else:
                        ClassResults.objects.create(
                        registration_number=group['registration_number'],
                        academic_year=group['entry_year'],
                        term=group['entry_term'],
                        entry_programme=group['entry_programme'],
                        entry_class=group['entry_class'],
                        stream_name=group['stream_name'],
                        full_name=group['full_name'],
                        subjects=subjects,
                        scores=scores,
                        average=group['average'],
                        grade=group['grade'],
                       remark=group['remark'],
                       position=group['position']
                )
                        
                        
                        
                   
            messages.success(request, "Results added successfully!")
            return redirect('admin:index')  # Redirect to the admin homepage

        except Exception as e:
            messages.error(request, f"Error adding results: {str(e)}")
            return redirect('admin:index')  # Redirect back to the results form

    else:
        messages.error(request, "Invalid request method.")
        return redirect('admin:index')  # Redirect back if not POST


 


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
from django.db import models

def save_assessment(request):
    if request.method == 'POST':
        registration_number = request.POST.get('registration_number')
        entry_year = request.POST.get('entry_year')
        entry_term = request.POST.get('entry_term')
        full_name = request.POST.get('full_name')

        try:
            with transaction.atomic():
                for key, value in request.POST.items():
                    
                    if key.startswith(('te_', 'ane_', 'mtt2_', 'mtt1_','mte_')):
                        subject_id = key.split('_')[1]

                        try:
                            subject = Subject.objects.get(id=subject_id)
                        except Subject.DoesNotExist:
                            continue

                        subject_name = request.POST.get(f'subject_name_{subject_id}')
                        te = float(request.POST.get(f'te_{subject_id}', 0) or 0)
                        ane = float(request.POST.get(f'ane_{subject_id}', 0) or 0)
                        mtt2 = float(request.POST.get(f'mtt2_{subject_id}', 0) or 0)
                        mtt1 = float(request.POST.get(f'mtt1_{subject_id}', 0) or 0)
                        mte = float(request.POST.get(f'mte_{subject_id}', 0) or 0)
                     
                        
                        total = 0
                        average = 0
                   
                        values = [te,ane,mtt2,mtt1,mte]
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
                            
                            result_que.te != te or 
                            result_que.ane != ane or 
                            result_que.mtt2 != mtt2 or 
                            result_que.mtt1 != mtt1 or 
                            result_que.mte !=mte or
                            result_que.average != average or 
                            result_que.grade != grade or 
                            result_que.remark != remark or 
                            result_que.full_name != full_name
                        ):
                            result_que.te = te
                            result_que.ane = ane
                            result_que.mtt2 = mtt2
                            result_que.mtt1 = mtt1
                            result_que.mte = mte
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
        entry_year_ = request.POST.get("entry_year")
        entry_term = request.POST.get("entry_term")
        entry_programme = request.POST.get("entry_programme")
        entry_class = request.POST.get("entry_class")
        stream_name = request.POST.get("stream_name")
        
        entry_year = entry_year_.split(' ')[0]
      
        
      
        

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