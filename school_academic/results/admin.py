from django.contrib import admin
from requests import request
from results.models import Result


# admin.py
from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from admission.models import StudentRegistration
from main_setting.models import AcademicYear, Class, Programme, Stream, Term
from .models import Result  # Adjust based on your model location

class ResultAdmin(admin.ModelAdmin):
    
    change_list_template = "admin/results_filter.html"
    
    def changelist_view(self, request, extra_context=None):
        academic_year = AcademicYear.objects.all()
        term = Term.objects.all()
        programmes = Programme.objects.all()
        classes = Class.objects.all()
        stream = Stream.objects.all()
        students = StudentRegistration.objects.all()
        
        extra_context = extra_context or {}
        extra_context.update({
            "academic_year": academic_year,
            "term": term,
            "programmes": programmes,
            "classes": classes,
            "stream": stream,
            "students": students,
            "title": "View results based on the following ",
        })
        
        return super().changelist_view(request, extra_context=extra_context)


    def has_add_permission(self, request):
        return False  # Disable adding new results

    


# admin.site.register(Result, ResultAdmin)


from django.contrib import admin
from .models import ExaminationResult

from django.contrib import admin
from django.utils.html import format_html
from .models import ExaminationResult
from django.contrib import admin
from django.urls import path
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa


from django.contrib import admin
from django.utils.html import format_html
from .models import ExaminationResult

from django.urls import reverse
from django.utils.html import format_html

from django.urls import reverse
from django.utils.html import format_html

class ExaminationResultAdmin(admin.ModelAdmin):
    list_display = ('exam_type',)

    def results_button(self, obj):
        url = reverse("examination_results_pdf", args=[obj.id])
        return format_html('<a class="button" href="{}">Results</a>', url)

    results_button.short_description = "Results"
    results_button.allow_tags = True

# admin.site.register(ExaminationResult, ExaminationResultAdmin)










# from django.contrib import admin
# from .models import ExamResults
# from django.contrib import admin
# from django.urls import reverse
# from django.utils.html import format_html


# from django.http import HttpResponse
# from django.template.loader import render_to_string
# import weasyprint
# from .models import Result
# from django.contrib import admin
# from django.templatetags.static import static


# @admin.register(ExamResults)
# class ExamResultsAdmin(admin.ModelAdmin):
#     change_list_template = 'admin/results.html'
  
#     def changelist_view(self, request, extra_context=None):
#         # Check if 'download=pdf' is in the URL
#         if request.GET.get('download') == 'pdf':
#             return self.download_pdf(request)
        
#         results = Result.objects.all()
#         extra_context = extra_context or {}
#         extra_context['results'] = results
#         return super().changelist_view(request, extra_context=extra_context)

#     def download_pdf(self, request):
#         # Generate the PDF with WeasyPrint
#         results = Result.objects.all()
#         html = render_to_string('admin/results.html', {'results': results})
        
#         # css_url = static('css/pdf_styles.css')  # Load CSS from static files
#         # css = weasyprint.CSS(css_url)  # Apply CSS
        
#         response = HttpResponse(content_type='application/pdf')
#         response['Content-Disposition'] = 'attachment; filename="exam_results.pdf"'
#         weasyprint.HTML(string=html).write_pdf(response)
        
#         # weasyprint.HTML(string=html).write_pdf(response, stylesheets=[css])
        
#         return response

#     def has_add_permission(self, request):
#         return False




