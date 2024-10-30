# views.py
from django.shortcuts import render, redirect, get_object_or_404


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