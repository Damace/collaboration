from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.utils import timezone
from .models import Student, Subject  # Assuming Subject and Student models are created

def generate_report(request, student_id):
    student = Student.objects.get(pk=student_id)
    subjects = Subject.objects.filter(student=student)
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
    student = Student.objects.get(pk=student_id)
    subjects = Subject.objects.filter(student=student)
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

