# urls.py

from django.urls import path
from . import views

urlpatterns = [
   
    path('add_students_assessments/', views.add_assessments_view,name='add_students_assessments'), 
    path('success/', views.success_page, name='success_page'),
    path('add_results/', views.add_results_view, name='add_results'),


]


