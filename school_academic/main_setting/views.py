# views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Department

def department_list(request):
    departments = Department.objects.all()
    return render(request, 'department_list.html', {'departments': departments})

def department_create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        if name:
            Department.objects.create(name=name)
            return redirect('department_list')
    
    return render(request, 'department_form.html')

def department_update(request, pk):
    department = get_object_or_404(Department, pk=pk)
    if request.method == 'POST':
        department.name = request.POST.get('name')
        department.save()
        return redirect('department_list')
    
    return render(request, 'department_form.html', {'department': department})

def department_delete(request, pk):
    department = get_object_or_404(Department, pk=pk)
    if request.method == 'POST':
        department.delete()
        return redirect('department_list')
    
    return render(request, 'department_confirm_delete.html', {'department': department})

############################################################

# views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Programme

def programme_list(request):
    programmes = Programme.objects.all()
    return render(request, 'programme_list.html', {'programmes': programmes})

def programme_create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        if name:
            Programme.objects.create(name=name)
            return redirect('programme_list')
    
    return render(request, 'programme_form.html')

def programme_update(request, pk):
    programme = get_object_or_404(Programme, pk=pk)
    if request.method == 'POST':
        programme.name = request.POST.get('name')
        programme.save()
        return redirect('programme_list')
    
    return render(request, 'programme_form.html', {'programme': programme})

def programme_delete(request, pk):
    programme = get_object_or_404(Programme, pk=pk)
    if request.method == 'POST':
        programme.delete()
        return redirect('programme_list')
    
    return render(request, 'programme_confirm_delete.html', {'programme': programme})

############################################################


# views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Subject, Department

def subject_list(request):
    subjects = Subject.objects.all()
    return render(request, 'subject_list.html', {'subjects': subjects})

def subject_create(request):
    if request.method == 'POST':
        department_id = request.POST.get('department')
        subject_code = request.POST.get('subject_code')
        subject_name = request.POST.get('subject_name')
        
        if department_id and subject_code and subject_name:
            department = get_object_or_404(Department, pk=department_id)
            Subject.objects.create(department=department, subject_code=subject_code, subject_name=subject_name)
            return redirect('subject_list')

    departments = Department.objects.all()
    return render(request, 'subject_form.html', {'departments': departments})

def subject_update(request, pk):
    subject = get_object_or_404(Subject, pk=pk)
    if request.method == 'POST':
        subject.department_id = request.POST.get('department')
        subject.subject_code = request.POST.get('subject_code')
        subject.subject_name = request.POST.get('subject_name')
        subject.save()
        return redirect('subject_list')

    departments = Department.objects.all()
    return render(request, 'subject_form.html', {'subject': subject, 'departments': departments})

def subject_delete(request, pk):
    subject = get_object_or_404(Subject, pk=pk)
    if request.method == 'POST':
        subject.delete()
        return redirect('subject_list')
    
    return render(request, 'subject_confirm_delete.html', {'subject': subject})

############################################

from django.shortcuts import render

# Create your views here.
# views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Class

def class_list(request):
    classes = Class.objects.all()
    return render(request, 'class_list.html', {'classes': classes})

def class_create(request):
    if request.method == 'POST':
        program_name = request.POST.get('program_name')
        class_name = request.POST.get('class_name')
        no_of_streams = request.POST.get('no_of_streams')
        name_of_streams = request.POST.get('name_of_streams')
        
        if program_name and class_name and no_of_streams and name_of_streams:
            Class.objects.create(
                program_name=program_name,
                class_name=class_name,
                no_of_streams=no_of_streams,
                name_of_streams=name_of_streams
            )
            return redirect('class_list')

    return render(request, 'class_form.html')

def class_update(request, pk):
    class_instance = get_object_or_404(Class, pk=pk)
    if request.method == 'POST':
        class_instance.program_name = request.POST.get('program_name')
        class_instance.class_name = request.POST.get('class_name')
        class_instance.no_of_streams = request.POST.get('no_of_streams')
        class_instance.name_of_streams = request.POST.get('name_of_streams')
        class_instance.save()
        return redirect('class_list')

    return render(request, 'class_form.html', {'class_instance': class_instance})

def class_delete(request, pk):
    class_instance = get_object_or_404(Class, pk=pk)
    if request.method == 'POST':
        class_instance.delete()
        return redirect('class_list')
    
    return render(request, 'class_confirm_delete.html', {'class_instance': class_instance})


############################################

# views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Term

def term_list(request):
    terms = Term.objects.all()
    return render(request, 'term_list.html', {'terms': terms})

def term_create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        
        if name:
            Term.objects.create(name=name)
            return redirect('term_list')

    return render(request, 'term_form.html')

def term_update(request, pk):
    term = get_object_or_404(Term, pk=pk)
    if request.method == 'POST':
        term.name = request.POST.get('name')
        term.save()
        return redirect('term_list')

    return render(request, 'term_form.html', {'term': term})

def term_delete(request, pk):
    term = get_object_or_404(Term, pk=pk)
    if request.method == 'POST':
        term.delete()
        return redirect('term_list')
    
    return render(request, 'term_confirm_delete.html', {'term': term})

##################################################################################

from django.shortcuts import render

# Create your views here.
# views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import AcademicYear

def academic_year_list(request):
    years = AcademicYear.objects.all()
    return render(request, 'academic_year_list.html', {'years': years})

def academic_year_create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        status = request.POST.get('status')
        
        if name and status:
            AcademicYear.objects.create(name=name, status=status)
            return redirect('academic_year_list')

    return render(request, 'academic_year_form.html')

def academic_year_update(request, pk):
    year = get_object_or_404(AcademicYear, pk=pk)
    if request.method == 'POST':
        year.name = request.POST.get('name')
        year.status = request.POST.get('status')
        year.save()
        return redirect('academic_year_list')

    return render(request, 'academic_year_form.html', {'year': year})

def academic_year_delete(request, pk):
    year = get_object_or_404(AcademicYear, pk=pk)
    if request.method == 'POST':
        year.delete()
        return redirect('academic_year_list')
    
    return render(request, 'academic_year_confirm_delete.html', {'year': year})


################################################################################

from django.shortcuts import render

# Create your views here.
# views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Assessment

def assessment_list(request):
    assessments = Assessment.objects.all()
    return render(request, 'assessment_list.html', {'assessments': assessments})

def assessment_create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        
        if name:
            Assessment.objects.create(name=name)
            return redirect('assessment_list')

    return render(request, 'assessment_form.html')

def assessment_update(request, pk):
    assessment = get_object_or_404(Assessment, pk=pk)
    if request.method == 'POST':
        assessment.name = request.POST.get('name')
        assessment.save()
        return redirect('assessment_list')

    return render(request, 'assessment_form.html', {'assessment': assessment})

def assessment_delete(request, pk):
    assessment = get_object_or_404(Assessment, pk=pk)
    if request.method == 'POST':
        assessment.delete()
        return redirect('assessment_list')
    
    return render(request, 'assessment_confirm_delete.html', {'assessment': assessment})