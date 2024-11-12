from django.urls import path
from . import views

urlpatterns = [
    path('report/<int:student_id>/', views.generate_report, name='generate_report'),
    path('report/pdf/<int:student_id>/', views.generate_pdf_report, name='generate_pdf_report'),
]
