from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from .models import Result
from weasyprint import HTML
from django.template.loader import render_to_string

def results_view(request):
    # Retrieve all results
    results = Result.objects.all()
    context = {
        'results': results
    }
    
    # Render the HTML template
    return render(request, 'results.html', context)

def download_results_pdf(request):
    results = Result.objects.all()
    context = {
        'results': results
    }
    
    # Render the HTML to string
    html_string = render_to_string('results.html', context)
    
    # Create a PDF from the HTML
    pdf = HTML(string=html_string).write_pdf()
    
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="results.pdf"'
    return response



from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import ExaminationResult, Result
from io import BytesIO
from django.template.loader import get_template
from xhtml2pdf import pisa

def examination_results_pdf(request, exam_id):
    # Fetch the specific ExaminationResult and corresponding Results
    examination_result = get_object_or_404(ExaminationResult, id=exam_id)
    results = Result.objects.filter(class_name=examination_result.exam_category)

    # Render the HTML template with context data
    template = get_template("admin/examinationResults.html")
    html = template.render({"examination_result": examination_result, "results": results})

    # Generate the PDF
    response = HttpResponse(content_type="application/pdf")
    response["Content-Disposition"] = f'attachment; filename="{examination_result.exam_category}_results.pdf"'

    # Convert HTML to PDF
    pisa_status = pisa.CreatePDF(BytesIO(html.encode("UTF-8")), dest=response)

    # Check for errors in the PDF generation process
    if pisa_status.err:
        return HttpResponse("Error generating PDF", status=500)

    return response



