from django.contrib import admin
from django.urls import path
from systemUsers.views import custom_admin_login_view,custom_logout


urlpatterns = [
    path('', custom_admin_login_view, name='custom_admin_login'),
    path('admin/', admin.site.urls), 
    path('admin_logout/', custom_logout, name='admin_logout'),
   
    
]
 
