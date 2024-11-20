# urls.py

from django.urls import path
from . import views

urlpatterns = [
   
    path('add_students_assessments/', views.add_assessments_view,name='add_students_assessments'), 
    path('success/', views.success_page, name='success_page'),
    path('add_results/', views.add_results_view, name='add_results'),
    path('add-assessment/<str:registration_number>/', views.add_assessment, name='add_assessment'),
    path('save-assessment/', views.save_assessment, name='save_assessment'),


]


