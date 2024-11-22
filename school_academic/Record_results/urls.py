# urls.py

from django.urls import path
from . import views

urlpatterns = [
   
    path('add_students_assessments/', views.add_assessments_view,name='add_students_assessments'), 
    path('success/', views.success_page, name='success_page'),
    path('add_results/', views.add_results_view, name='add_results'),
    path('add-assessment/<str:registration_number>/', views.add_assessment, name='add_assessment'),
    
    path('add-assessment2/<str:registration_number>/', views.add_assessment2, name='add_assessment2'),
    path('save-assessment/', views.save_assessment, name='save_assessment'),
    path('save-assessment2/', views.save_assessment2, name='save_assessment2'),


]


