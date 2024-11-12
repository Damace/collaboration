# urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('add-results/', views.add_results_view, name='add_results'),  
    path('add_assessments/', views.add_assessments_view,name='add_assessments'), 
    path('success/', views.success_page, name='success_page'),
]
