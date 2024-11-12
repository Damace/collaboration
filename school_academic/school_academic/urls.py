
from django.contrib import admin
from django.urls import path

from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.urls import path

urlpatterns = [
    # path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('admin/', admin.site.urls),
    # path('', include('results.urls')),
    # path('', include('Record_results.urls')),
    path('', include('systemUsers.urls')),
    
  
   
]


