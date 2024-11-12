from django.urls import path
from .views import results_view,examination_results_pdf
from . import views

urlpatterns = [
    path('results/', results_view, name='results'),
    
    # path("examination-results/<int:exam_id>/pdf/", views.examination_results_pdf, name="examination_results_pdf"),
    
    path('results/download/<int:result_id>/', examination_results_pdf, name='results'),  # Ensure this name matches
]


