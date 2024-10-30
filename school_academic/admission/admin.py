# admin.py
from django.contrib import admin

from admission.filters import StudentFilter
from .models import Sponsor

class SponsorAdmin(admin.ModelAdmin):
    list_display = ('sponsor_name', 'mobile', 'email', 'postal_address', 'physical_address')
    search_fields = ('sponsor_name', 'email', 'mobile')

admin.site.register(Sponsor, SponsorAdmin)


# admin.py
from django.contrib import admin
from .models import EntryCategory

class EntryCategoryAdmin(admin.ModelAdmin):
    list_display = ('entry_category',)
    search_fields = ('entry_category',)
    ordering = ('entry_category',)

admin.site.register(EntryCategory, EntryCategoryAdmin)


# systemUsers/admin.py
from django.contrib import admin
from .models import StudentRegistration

# class StudentRegistrationAdmin(admin.ModelAdmin):
#     list_display = ('registration_number', 'first_name', 'last_name', 'entry_year', 'entry_programme', 'entry_class')
#     search_fields = ('registration_number', 'first_name', 'last_name')
#     list_filter = ('entry_year', 'entry_term', 'entry_programme', 'entry_class')

#     fieldsets = (
#         ('Personal Particulars', {
#             'fields': (
#                 'entry_year', 'entry_term', 'entry_programme', 'entry_class', 'entry_category',
#                 'sponsor_name', 'registration_number', 'first_name', 'last_name', 'other_name',
#                 'gender', 'birth_date', 'nationality', 'disability'
#             )
#         }),
#         ('Next of Kin 1', {
#             'fields': (
#                 'next_of_kin1_name', 'next_of_kin1_mobile_number', 'next_of_kin1_email', 'next_of_kin1_postal_address'
#             )
#         }),
#         ('Next of Kin 2', {
#             'fields': (
#                 'next_of_kin2_name', 'next_of_kin2_mobile_number', 'next_of_kin2_email', 'next_of_kin2_postal_address',
#                 'next_of_kin2_profile_picture'
#             )
#         }),
#     )

# admin.site.register(StudentRegistration, StudentRegistrationAdmin)


from django.contrib import admin
from .models import StudentRegistration
from .filters import StudentFilter

class StudentRegistrationAdmin(admin.ModelAdmin):
    list_display = ('registration_number', 'first_name', 'last_name', 'entry_year', 'entry_programme', 'entry_class')
    search_fields = ('name',)

    def changelist_view(self, request, extra_context=None):
        # Create an instance of the filter
        student_filter = StudentFilter(request.GET, queryset=StudentRegistration.objects.all())
        context = {
            'filter': student_filter,
        }
        return super().changelist_view(request, extra_context=context)

admin.site.register(StudentRegistration, StudentRegistrationAdmin)


















# from django.contrib import admin
# from django.utils.translation import gettext_lazy as _
# from .models import StudentRegistration  # Assuming StudentRegistration exists

# class MultiSelectFilter(admin.SimpleListFilter):
#     template = 'admin/multi_select_filter.html'  # Custom template for multi-select

#     def lookups(self, request, model_admin):
#         return self.get_lookups()

#     def queryset(self, request, queryset):
#         values = request.GET.getlist(self.parameter_name)
#         if values:
#             return queryset.filter(**{f'{self.parameter_name}__in': values})
#         return queryset

# class EntryYearFilter(MultiSelectFilter):
#     title = _('Entry Year')
#     parameter_name = 'entry_year'

#     def get_lookups(self):
#         return StudentRegistration.objects.values_list('entry_year', 'entry_year').distinct()

# class EntryTermFilter(MultiSelectFilter):
#     title = _('Entry Term')
#     parameter_name = 'entry_term'

#     def get_lookups(self):
#         return StudentRegistration.objects.values_list('entry_term', 'entry_term').distinct()

# class EntryProgrammeFilter(MultiSelectFilter):
#     title = _('Entry Programme')
#     parameter_name = 'entry_programme'

#     def get_lookups(self):
#         return StudentRegistration.objects.values_list('entry_programme', 'entry_programme').distinct()

# class EntryClassFilter(MultiSelectFilter):
#     title = _('Entry Class')
#     parameter_name = 'entry_class'

#     def get_lookups(self):
#         return StudentRegistration.objects.values_list('entry_class', 'entry_class').distinct()



# class StudentRegistrationAdmin(admin.ModelAdmin):
#     list_display = ('entry_year', 'entry_term', 'entry_programme', 'entry_class')
#     list_filter = (EntryYearFilter, EntryTermFilter, EntryProgrammeFilter, EntryClassFilter)

# admin.site.register(StudentRegistration, StudentRegistrationAdmin)

# systemUsers/admin.py

from django.contrib import admin
 # Import your filter class
from django_filters import FilterSet

class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'student_class', 'class_stream')  # Customize this as needed
    list_filter = (StudentFilter,)  # Add your filter class here

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset

# admin.site.register(StudentRegistration, StudentAdmin)


# from django.contrib import admin
# from .models import StudentRegistration, AcademicYear, Term, Programme, Class, Stream
# from .filters import StudentFilter

# class StudentRegistrationAdmin(admin.ModelAdmin):
#     list_display = ('name', 'academic_year', 'term', 'programme', 'student_class', 'class_stream')
#     search_fields = ('name',)

#     def changelist_view(self, request, extra_context=None):
#         # Create an instance of the filter
#         student_filter = StudentFilter(request.GET, queryset=StudentRegistration.objects.all())
#         return super().changelist_view(request, extra_context={'filter': student_filter})

# admin.site.register(StudentRegistration, StudentRegistrationAdmin)
# admin.site.register(AcademicYear)
# admin.site.register(Term)
# admin.site.register(Programme)
# admin.site.register(Class)
# admin.site.register(Stream)


























# systemUsers/admin.py
from django.contrib import admin
from django.contrib import messages
from .models import ImportStudent, StudentRegistration
from .utils import import_students_from_file

@admin.register(ImportStudent)
class ImportStudentAdmin(admin.ModelAdmin):
    list_display = ('file', 'uploaded_at')
    actions = ['process_import_file']

    def process_import_file(self, request, queryset):
        for import_file in queryset:
            file_path = import_file.file.path
            try:
                import_students_from_file(file_path)
                self.message_user(request, f'Successfully imported students from {import_file.file.name}', messages.SUCCESS)
            except Exception as e:
                self.message_user(request, f'Error importing {import_file.file.name}: {e}', messages.ERROR)

    process_import_file.short_description = "Process selected import files"


# systemUsers/admin.py
from django.contrib import admin
from django import forms
from .models import UpgradeStudent, Stream, Class

class UpgradeStudentAdminForm(forms.ModelForm):
    class Meta:
        model = UpgradeStudent
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'student_class' in self.data:
            try:
                class_id = int(self.data.get('student_class'))
                self.fields['class_stream'].queryset = Stream.objects.filter(class_id=class_id)
            except (ValueError, TypeError):
                pass  # Invalid input or no class selected
        elif self.instance.pk:
            self.fields['class_stream'].queryset = self.instance.student_class.stream_set.all()

class UpgradeStudentAdmin(admin.ModelAdmin):
    form = UpgradeStudentAdminForm
    list_display = ('academic_year', 'term', 'programme', 'student_class', 'class_stream')

admin.site.register(UpgradeStudent, UpgradeStudentAdmin)



