# urls.py
from django.urls import path
from .views import sponsor_list, sponsor_create, sponsor_update, sponsor_delete

from django.urls import path
from .views import custom_filter_view, get_streams
from django.urls import path
from .views import generate_pdf
from admission import views
from django.urls import path
from .views import registration_data, second_chart_data
from django.urls import path
from .views import registration_bar_graph
from django.urls import path
from .views import student_count_bar_chart

urlpatterns = [
    path('', sponsor_list, name='sponsor_list'),
    path('sponsor/new/', sponsor_create, name='sponsor_create'),
    path('sponsor/edit/<int:pk>/', sponsor_update, name='sponsor_update'),
    path('sponsor/delete/<int:pk>/', sponsor_delete, name='sponsor_delete'),
    path('custom_filter/', custom_filter_view, name='custom_filter'),
    path('get_streams/<int:class_id>/', get_streams, name='get_streams'),
    path('generate_pdf/', generate_pdf, name='generate_pdf'),

    # path('admin/promote-students/', views.promote_students_view, name='promote_students'),
    
     path('registration-data/', registration_data, name='registration_data'),
     path('second-chart-data/', second_chart_data, name='second_chart_data'),
     path("results_data/", views.results_data, name="results_data"),# Add this line
     path('all-students/', views.all_students, name='all_students'),
     path('upgrade_students/', views.upgrade_students_view, name='upgrade_students'),
     path('registration-graph/', registration_bar_graph, name='registration_graph'),
     path('student-chart/', student_count_bar_chart, name='student_count_bar_chart'),
]


