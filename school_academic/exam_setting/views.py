# views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import GradeScale, Program

def grade_scale_list(request):
    grade_scales = GradeScale.objects.all()
    return render(request, 'grade_scale_list.html', {'grade_scales': grade_scales})

def grade_scale_create(request):
    if request.method == 'POST':
        program_name = request.POST.get('program_name')
        grade_name = request.POST.get('grade_name')
        minimum_marks = request.POST.get('minimum_marks')
        grade_point = request.POST.get('grade_point')
        remark = request.POST.get('remark')
        sequence_order = request.POST.get('sequence_order')

        if all([program_name, grade_name, minimum_marks, grade_point, remark, sequence_order]):
            GradeScale.objects.create(
                program_name=Program.objects.get(pk=program_name),
                grade_name=grade_name,
                minimum_marks=minimum_marks,
                grade_point=grade_point,
                remark=remark,
                sequence_order=sequence_order
            )
            return redirect('grade_scale_list')

    programs = Program.objects.all()
    return render(request, 'grade_scale_form.html', {'programs': programs})

def grade_scale_update(request, pk):
    grade_scale = get_object_or_404(GradeScale, pk=pk)
    if request.method == 'POST':
        grade_scale.program_name = Program.objects.get(pk=request.POST.get('program_name'))
        grade_scale.grade_name = request.POST.get('grade_name')
        grade_scale.minimum_marks = request.POST.get('minimum_marks')
        grade_scale.grade_point = request.POST.get('grade_point')
        grade_scale.remark = request.POST.get('remark')
        grade_scale.sequence_order = request.POST.get('sequence_order')
        grade_scale.save()
        return redirect('grade_scale_list')

    programs = Program.objects.all()
    return render(request, 'grade_scale_form.html', {'grade_scale': grade_scale, 'programs': programs})

def grade_scale_delete(request, pk):
    grade_scale = get_object_or_404(GradeScale, pk=pk)
    if request.method == 'POST':
        grade_scale.delete()
        return redirect('grade_scale_list')
    
    return render(request, 'grade_scale_confirm_delete.html', {'grade_scale': grade_scale})


######################################################

# views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import GradeDivision, Program

def grade_division_list(request):
    grade_divisions = GradeDivision.objects.all()
    return render(request, 'grade_division_list.html', {'grade_divisions': grade_divisions})

def grade_division_create(request):
    if request.method == 'POST':
        program_name = request.POST.get('program_name')
        grade_name = request.POST.get('grade_name')
        division_title = request.POST.get('division_title')
        minimum_division_point = request.POST.get('minimum_division_point')
        sequence_order = request.POST.get('sequence_order')

        if all([program_name, grade_name, division_title, minimum_division_point, sequence_order]):
            GradeDivision.objects.create(
                program_name=Program.objects.get(pk=program_name),
                grade_name=grade_name,
                division_title=division_title,
                minimum_division_point=minimum_division_point,
                sequence_order=sequence_order
            )
            return redirect('grade_division_list')

    programs = Program.objects.all()
    return render(request, 'grade_division_form.html', {'programs': programs})

def grade_division_update(request, pk):
    grade_division = get_object_or_404(GradeDivision, pk=pk)
    if request.method == 'POST':
        grade_division.program_name = Program.objects.get(pk=request.POST.get('program_name'))
        grade_division.grade_name = request.POST.get('grade_name')
        grade_division.division_title = request.POST.get('division_title')
        grade_division.minimum_division_point = request.POST.get('minimum_division_point')
        grade_division.sequence_order = request.POST.get('sequence_order')
        grade_division.save()
        return redirect('grade_division_list')

    programs = Program.objects.all()
    return render(request, 'grade_division_form.html', {'grade_division': grade_division, 'programs': programs})

def grade_division_delete(request, pk):
    grade_division = get_object_or_404(GradeDivision, pk=pk)
    if request.method == 'POST':
        grade_division.delete()
        return redirect('grade_division_list')
    
    return render(request, 'grade_division_confirm_delete.html', {'grade_division': grade_division})

########################################################################


from django.shortcuts import render

# Create your views here.
# views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import ExamsCategory

def exams_category_list(request):
    exams_categories = ExamsCategory.objects.all()
    return render(request, 'exams_category_list.html', {'exams_categories': exams_categories})

def exams_category_create(request):
    if request.method == 'POST':
        short_name = request.POST.get('short_name')
        name = request.POST.get('name')
        mandatory = request.POST.get('mandatory') == 'yes'  # Convert to boolean

        if all([short_name, name]):
            ExamsCategory.objects.create(
                short_name=short_name,
                name=name,
                mandatory=mandatory
            )
            return redirect('exams_category_list')

    return render(request, 'exams_category_form.html')

def exams_category_update(request, pk):
    exams_category = get_object_or_404(ExamsCategory, pk=pk)
    if request.method == 'POST':
        exams_category.short_name = request.POST.get('short_name')
        exams_category.name = request.POST.get('name')
        exams_category.mandatory = request.POST.get('mandatory') == 'yes'  # Convert to boolean
        exams_category.save()
        return redirect('exams_category_list')

    return render(request, 'exams_category_form.html', {'exams_category': exams_category})

def exams_category_delete(request, pk):
    exams_category = get_object_or_404(ExamsCategory, pk=pk)
    if request.method == 'POST':
        exams_category.delete()
        return redirect('exams_category_list')
    
    return render(request, 'exams_category_confirm_delete.html', {'exams_category': exams_category})