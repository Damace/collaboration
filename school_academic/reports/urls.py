from django.urls import path
from . import views

urlpatterns = [
    path('report/<int:student_id>/', views.generate_report, name='generate_report'),
    path('report/pdf/<int:student_id>/', views.generate_pdf_report, name='generate_pdf_report'),
    path('view_result/<str:registration_number>/<str:academic_year>/<str:term>/', views.download_assessment, name='view_result'),
]



