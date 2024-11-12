from django.contrib import admin
from .models import RecordAttendanceProxy


from .models import AbsentReason

@admin.register(AbsentReason)
class AbsentReasonAdmin(admin.ModelAdmin):
    list_display = ('name',)

class RecordAttendanceProxyAdmin(admin.ModelAdmin):
    list_display = ('registration_number', 'first_name', 'last_name')
    list_filter = ('entry_year', 'entry_programme', 'entry_class')
    search_fields = ('registration_number', 'first_name', 'last_name')
    actions = ['promote_students_action']

    def promote_students_action(self, request, queryset):
        # Your action logic here
        pass

# Register the proxy model and admin class
admin.site.register(RecordAttendanceProxy, RecordAttendanceProxyAdmin)


from django.contrib import admin
from .models import StudentAssignment

from django.contrib import admin
from .models import StudentAssignment

class StudentAssignmentAdmin(admin.ModelAdmin):
    list_display = ('subject_name', 'deadline_date', 'remark', 'upload_assignment')
    search_fields = ('subject_name__name', 'remark')
    list_filter = ('deadline_date', 'subject_name')
    date_hierarchy = 'deadline_date'

admin.site.register(StudentAssignment, StudentAssignmentAdmin)
