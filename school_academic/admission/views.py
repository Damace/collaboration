# views.py
from django.shortcuts import render, redirect, get_object_or_404

from results.models import Result

from .models import Sponsor


def sponsor_list(request):
    sponsors = Sponsor.objects.all()
    return render(request, 'sponsor_list.html', {'sponsors': sponsors})

def sponsor_create(request):
    if request.method == 'POST':
        sponsor_name = request.POST.get('sponsor_name')
        mobile = request.POST.get('mobile')
        email = request.POST.get('email')
        postal_address = request.POST.get('postal_address')
        physical_address = request.POST.get('physical_address')

        sponsor = Sponsor(
            sponsor_name=sponsor_name,
            mobile=mobile,
            email=email,
            postal_address=postal_address,
            physical_address=physical_address
        )
        sponsor.save()
        return redirect('sponsor_list')
    
    return render(request, 'sponsor_form.html', {})

def sponsor_update(request, pk):
    sponsor = get_object_or_404(Sponsor, pk=pk)
    if request.method == 'POST':
        sponsor.sponsor_name = request.POST.get('sponsor_name')
        sponsor.mobile = request.POST.get('mobile')
        sponsor.email = request.POST.get('email')
        sponsor.postal_address = request.POST.get('postal_address')
        sponsor.physical_address = request.POST.get('physical_address')
        sponsor.save()
        return redirect('sponsor_list')
    
    return render(request, 'sponsor_form.html', {'sponsor': sponsor})

def sponsor_delete(request, pk):
    sponsor = get_object_or_404(Sponsor, pk=pk)
    if request.method == 'POST':
        sponsor.delete()
        return redirect('sponsor_list')
    
    return render(request, 'sponsor_confirm_delete.html', {'sponsor': sponsor})



from django.shortcuts import render
from django.http import JsonResponse
from .models import StudentRegistration, Stream
from .filters import StudentFilter

def custom_filter_view(request):
    student_filter = StudentFilter(request.GET, queryset=StudentRegistration.objects.all())
    return render(request, 'custom_filter.html', {'filter': student_filter})

def get_streams(request, class_id):
    streams = Stream.objects.filter(class_name_id=class_id).values('id', 'name')
    return JsonResponse({'streams': list(streams)})


from django.http import HttpResponse
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib import colors
from .models import StudentRegistration
from django.http import HttpResponse
# from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.pdfgen import canvas
from .models import StudentRegistration
from reportlab.lib.pagesizes import A4

from django.http import HttpResponse
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle



def generate_pdf(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="student_report.pdf"'

    # Create a PDF document
    pdf = SimpleDocTemplate(response, pagesize=A4)
    elements = []

       # Define custom styles
    styles = getSampleStyleSheet()
    
    title_style = ParagraphStyle(
        name='TitleStyle',
        fontSize=24,  # Font size for the title
        spaceAfter=12,
        alignment=1,  # Centered
        fontName='Helvetica-Bold'
    )
    
    header_style = ParagraphStyle(
        name='HeaderStyle',
        fontSize=18,  # Font size for the header
        spaceAfter=12,
        alignment=1,
        fontName='Helvetica-Bold'
    )
    
    normal_style = ParagraphStyle(
        name='NormalStyle',
        fontSize=12,  # Font size for normal text
        spaceAfter=6,
        alignment=0,  # Left-aligned
        fontName='Helvetica'
    )



        # Title and School Name
    styles = getSampleStyleSheet()
    title = Paragraph("Kondoa Girls Secondary School", styles['Title'])
    elements.append(title)

    header = Paragraph("Mock Examination Results - November 2023", styles['Heading2'])
    elements.append(header)


    # Adding a logo
    # logo_path = 'path/to/your/logo.png'  # Update with your logo path
    elements.append(Paragraph("<br/>", styles['Normal']))  # Add some space
    # elements.append(Paragraph("<img src='{}' width='200' height='80' />".format(logo_path), styles['Normal']))

    # Adding some space after the title and logo
    # elements.append(Paragraph("<br/><br/>", styles['Normal']))



    # Table data
    data = [['Full name', 'last_name','gender','Comb','Subject','Total','Average','Grade','point','Division','Comb pos','class pos']]
    students = StudentRegistration.objects.all()

    for student in students:
        data.append([
             Paragraph(student.first_name, styles['Normal']),
             Paragraph(student.last_name, styles['Normal']), 
             Paragraph(student.gender, styles['Normal']), 
            #  Paragraph(student.comb, styles['Normal']),
            #  Paragraph(student.subject, styles['Normal']),
            #  Paragraph(str(student.total), styles['Normal']),
            #  Paragraph(str(student.average), styles['Normal']),
            #  Paragraph(student.grade, styles['Normal']),
            #  Paragraph(str(student.point), styles['Normal']),
            #  Paragraph(student.division, styles['Normal']),
            #  Paragraph(str(student.comb_pos), styles['Normal']),
            #  Paragraph(str(student.class_pos), styles['Normal'])
            ])

    # students = students.objects.all()  # Fetch student results from the database
    # for index, student in enumerate(students, start=1):
    #     score = sum(student.scores.values()) / len(student.scores)  # Example calculation for average score
    #     position = index  # This should be calculated based on actual scores
    #     data.append([index, student.first_name + student.last_name, student.student_class, student.category, score, position])

    # Create a table
    table = Table(data)
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ]))


    elements.append(table)

    # Build the PDF and keep track of the page number
    pdf.build(elements, onFirstPage=add_page_number, onLaterPages=add_page_number)
    return response

def add_page_number(canvas, doc):
    # Set the position for the page number
    page_number = f"Page {doc.page}"

    # Draw the page number on the bottom center
    canvas.drawString(270, 10, page_number)




############ DEMOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO VIEW  


# views.py
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render

@staff_member_required  # Ensures only logged-in staff can access the view
def custom_report(request):
    context = {
        'data': "This is your custom report data.",
    }
    return render(request, 'admin/custom_report.html', context)




############ DEMOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO VIEW  




# views.py
from django.http import JsonResponse
from .models import StudentRegistration
from django.db.models import Count 

def registration_data(request):
    # Example: Count registrations per class
    data = StudentRegistration.objects.values('entry_class').annotate(count=Count('id'))
    
    classes = [item['entry_class'] for item in data]
    counts = [item['count'] for item in data]

    return JsonResponse({'classes': classes, 'counts': counts})

# views.py
# views.py
from django.http import JsonResponse
from django.db.models import Avg  # Import the Avg aggregation function
from .models import StudentRegistration

def second_chart_data(request):
    # Example data for the second chart
    data = StudentRegistration.objects.values('entry_class').annotate(average_score=Avg('entry_category'))  # Adjust 'score_field' to your actual field name
    classes = [item['entry_class'] for item in data]
    scores = [item['average_score'] for item in data]

    return JsonResponse({'classes': classes, 'scores': scores})


def results_data(request):
    # Aggregate average scores per subject
    data = Result.objects.values("subject").annotate(avg_score=Avg("total"))
    subjects = [item["subject"] for item in data]
    avg_scores = [item["avg_score"] for item in data]

    return JsonResponse({
        "subjects": subjects,
        "avg_scores": avg_scores
    })
    
    
from django.shortcuts import render


# views.py
from django.shortcuts import render
from .models import StudentRegistration

def all_students(request):
    students = StudentRegistration.objects.all()
    context = {
        'students': students,
    }
    return render(request, 'admin/filter_resultStudent.html', context)


# views.py

from django.shortcuts import render, redirect
from Record_results.models import QueResults
from django.shortcuts import redirect
from django.contrib import messages


def upgrade_students_view(request):
    if request.method == 'POST':
        # Get the selected criteria from the form
        academic_year_new = request.POST.get('academic_year_new')
        program_new = request.POST.get('programme_new')
        term_new = request.POST.get('term_new')
        class_new = request.POST.get('class_new')
        stream = request.POST.get('stream_new')
        
     
        # Process each selected student
        selected_students = request.POST.getlist('selected_students')
        for student_id in selected_students:
        
            student = StudentRegistration.objects.get(id=student_id)
            if academic_year_new:
                student.entry_year_id = academic_year_new
            if program_new:
                student.entry_programme_id = program_new
            if term_new:
                student.entry_term_id = term_new
            if class_new:
                student.entry_class_id = class_new
            if stream:
                student.stream_name_id = stream
            student.save()
            
            messages.success(request, "Upgraded successfully!")
        return redirect('admin:index')  # Redirect to the admin homepage 

    return render(request, 'addresults.html', {'filtered_students': ''})


import matplotlib.pyplot as plt
import numpy as np
from django.http import HttpResponse
from django.shortcuts import render
from io import BytesIO
import base64

def registration_bar_graph(request):
    # Query all students
    students = StudentRegistration.objects.all()
    
    # Extract registration numbers and names
    registration_numbers = [student.registration_number for student in students]
    names = [f"{student.first_name} {student.last_name}" for student in students]

    # Create a bar graph
    plt.figure(figsize=(10, 6))
    y_pos = np.arange(len(registration_numbers))
    plt.barh(y_pos, registration_numbers, align='center')
    plt.yticks(y_pos, names)
    plt.xlabel('Registration Number')
    plt.title('Student Registration Numbers')

    # Save the plot to a BytesIO object
    buf = BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    
    # Encode the image in base64
    image_png = buf.getvalue()
    graph = base64.b64encode(image_png).decode('utf-8')
    plt.close()

    return render(request, 'admin/index.html', {'graph': graph})


import matplotlib.pyplot as plt
import io
import urllib, base64
from django.shortcuts import render
from .models import StudentRegistration
from admission import models

def student_count_bar_chart(request):
    # Aggregate data: Count students by entry_class
    data = StudentRegistration.objects.values('entry_class').annotate(count=models.Count('id'))
    classes = [item['entry_class'] for item in data]
    counts = [item['count'] for item in data]

    # Generate bar chart
    plt.figure(figsize=(10, 6))
    plt.bar(classes, counts, color='skyblue')
    plt.xlabel('Class')
    plt.ylabel('Number of Registered Students')
    plt.title('Number of Registered Students per Class')
    plt.xticks(rotation=45)

    # Save chart to a bytes buffer
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    string = base64.b64encode(buf.read())
    uri = 'data:image/png;base64,' + urllib.parse.quote(string)
    plt.close()  # Close the plot to free memory

    return render(request, 'student_chart.html', {'data': uri})
