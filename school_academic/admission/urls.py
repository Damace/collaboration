# urls.py
from django.urls import path
from .views import sponsor_list, sponsor_create, sponsor_update, sponsor_delete

from django.urls import path
from .views import custom_filter_view, get_streams
from django.urls import path
from .views import generate_pdf

urlpatterns = [
    path('', sponsor_list, name='sponsor_list'),
    path('sponsor/new/', sponsor_create, name='sponsor_create'),
    path('sponsor/edit/<int:pk>/', sponsor_update, name='sponsor_update'),
    path('sponsor/delete/<int:pk>/', sponsor_delete, name='sponsor_delete'),
    path('custom_filter/', custom_filter_view, name='custom_filter'),
    path('get_streams/<int:class_id>/', get_streams, name='get_streams'),
    path('generate_pdf/', generate_pdf, name='generate_pdf'),
]



