from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('is_student',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('is_student',)}),
    )
    list_display = UserAdmin.list_display + ('is_student',) 

admin.site.register(CustomUser, CustomUserAdmin)


from django.contrib import admin
from .models import BulkSMS

@admin.register(BulkSMS)
class BulkSMSAdmin(admin.ModelAdmin):
    list_display = ('phone_number', 'created_at')
    search_fields = ('phone_number', 'message')
    list_filter = ('created_at',)
