# admin.py
from django.contrib import admin
from django.http import HttpResponseRedirect
from admission.filters import StudentFilter
from main_setting.models import Subject
from .models import Sponsor



from django.contrib import admin
from django.urls import path
from .views import custom_report


from django.contrib import admin
from django.contrib.auth.models import User, Group

# Unregister the User and Group models from the admin site
# admin.site.unregister(User)
admin.site.unregister(Group)


from django.contrib import admin
from django.utils.translation import gettext_lazy as _

# Customize the admin site
admin.site.site_header = _("Kondoa High")  # Header text
admin.site.site_title = _("Kondoa Girls")           # Title for browser tab
admin.site.index_title = _("Kondoa Girls")  # Dashboard title



class MyAdminSite(admin.AdminSite):

    site_header = "My Custom Admin"

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('custom-report/', self.admin_view(custom_report), name='custom_report'),
        ]
        return custom_urls + urls

admin_site = MyAdminSite(name='myadmin')

### %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%



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
from .models import StudentRegistration, AcademicYear, Term, Programme, Class, Stream  
    
from django.contrib import admin
from .models import StudentRegistration, UpgradeStudent  # Adjust the import based on your project structure

from django.contrib import admin
from .models import StudentRegistration, UpgradeStudent  # Adjust the import based on your project structure

from django.contrib import admin
from django.urls import path
from django.shortcuts import redirect
from django.utils.html import format_html
from django.contrib import messages
from .models import StudentRegistration
from django.contrib import admin, messages
from django.urls import path
from django.shortcuts import render, redirect
from django.urls import reverse                                                                                                                                                                                                                                   


##################################################################################################################################################

class AcademicYearFilter(admin.SimpleListFilter):
    title = 'Academic Year'
    parameter_name = 'academic_year'

    def lookups(self, request, model_admin):
        return [(year.id, year.name) for year in AcademicYear.objects.all()]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(entry_year__id=self.value())
        return queryset
    
class ProgrammeFilter(admin.SimpleListFilter):
    title = 'Programme'
    parameter_name = 'entry_programme'

    def lookups(self, request, model_admin):
        return [(programme.id, programme.name) for programme in Programme.objects.all()]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(entry_programme_id__in=self.value().split(','))
        return queryset
    
class TermFilter(admin.SimpleListFilter):
    title = 'Term'
    parameter_name = 'term'

    def lookups(self, request, model_admin):
        return [(term.id, term.name) for term in Term.objects.all()]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(entry_term__id=self.value())
        return queryset

class ClassFilter(admin.SimpleListFilter):
    title = 'Class'
    parameter_name = 'class'

    def lookups(self, request, model_admin):
        return [(cls.id, cls.class_name) for cls in Class.objects.all()]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(entry_class__id=self.value())
        return queryset

class StreamFilter(admin.SimpleListFilter):
    title = 'Stream'
    parameter_name = 'stream'

    def lookups(self, request, model_admin):
        return [(stream.id, stream.name) for stream in Stream.objects.all()]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(stream_name__id=self.value())
        return queryset

class SubjectFilter(admin.SimpleListFilter):
    title = 'Subject'
    parameter_name = 'subject'

    def lookups(self, request, model_admin):
        # Assuming that the `Subject` model has a `name` field for subject names
        return [(subject.id, subject.subject_name) for subject in Subject.objects.all()]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(subjects__id=self.value())  # Assuming `subjects` is the ManyToMany field
        return queryset



class ClassFilter(admin.SimpleListFilter):
    title = 'Class'
    parameter_name = 'entry_class'

    def lookups(self, request, model_admin):
        return [(cls.id, cls.class_name) for cls in Class.objects.all()]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(entry_class_id__in=self.value().split(','))
        return queryset


# class StreamFilter(admin.SimpleListFilter):
#     title = 'Stream'
#     parameter_name = 'class_stream'

#     def lookups(self, request, model_admin):
#         return [(stream.id, stream.name) for stream in Stream.objects.all()]

#     def queryset(self, request, queryset):
#         if self.value():
#             return queryset.filter(entry_stream_id__in=self.value().split(','))
#         return queryset
    

from .models import Class

class StudentClassFilter(admin.SimpleListFilter):
    title = 'Student Class'
    parameter_name = 'student_class'

    def lookups(self, request, model_admin):
        return [(cls.id, cls.class_name) for cls in Class.objects.all()]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(student_class_id=self.value())
        return queryset

from .models import Stream

class ClassStreamFilter(admin.SimpleListFilter):
    title = 'Class Stream'
    parameter_name = 'class_stream'

    def lookups(self, request, model_admin):
        return [(stream.id, stream.name) for stream in Stream.objects.all()]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(class_stream_id=self.value())
        return queryset 
    
class StudentRegistrationAdmin(admin.ModelAdmin):
    list_display = ('registration_number', 'first_name', 'last_name','entry_class','stream_name')
    list_filter = (AcademicYearFilter, ProgrammeFilter, TermFilter, ClassFilter,SubjectFilter)
    search_fields = ('registration_number', 'first_name', 'last_name')  
    actions = ['promote_students_action','add_results'] 
    
    
    # change_list_template = "admin/promote_students.html"  # Override template


    # Custom view for the promote students page
    def promote_students(self, request):
        if request.method == 'POST':
            # Get selected academic year, term, programme, and class from form
            academic_year_id = request.POST.get('academic_year')
            term_id = request.POST.get('term')
            programme_id = request.POST.get('programme')
            class_id = request.POST.get('class')

            # Fetch instances based on IDs from the form
            academic_year = AcademicYear.objects.get(id=academic_year_id)
            term = Term.objects.get(id=term_id)
            programme = Programme.objects.get(id=programme_id)
            new_class = Class.objects.get(id=class_id)

            # Get selected student IDs from session
            selected_student_ids = request.session.get('selected_student_ids', [])

            # Promote each selected student
            students = StudentRegistration.objects.filter(id__in=selected_student_ids)
            for student in students:
                student.entry_year = academic_year
                student.entry_term = term
                student.entry_programme = programme
                student.entry_class = new_class
                student.save()

            messages.success(request, f"Successfully promoted {students.count()} students.")
            return redirect('admin:admission_studentregistration_changelist')

        else:
            # Initial GET request - display promotion form
            context = {
                'academic_years': AcademicYear.objects.all(),
                'terms': Term.objects.all(),
                'programmes': Programme.objects.all(),
                # 'classes': Class.objects.all(),
            }
            return render(request, 'admin/promote_students.html', context)
        

    def promote_student(self, request, student_id):
        # Implement the logic to promote a student here
        messages.success(request, f"Student {student_id} promoted successfully.")
        return redirect("..")


    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('promote-students/', self.admin_site.admin_view(self.promote_students_view), name="promote-students"),
        ]
        return custom_urls + urls
        
    def promote_students_view(self, request):
        """Custom view to promote students"""
        if request.method == "POST":
            selected_students = request.POST.getlist("students")
            new_class = request.POST.get("new_class")

            if selected_students and new_class:
                # Apply promotion logic
                students = StudentRegistration.objects.filter(id__in=selected_students)
                students.update(entry_class=new_class)
                messages.success(request, f"Successfully promoted {students.count()} students to {new_class}.")
                return redirect("..")

            messages.error(request, "Please select students and a new class.")
        
        # Context for the promotion page
        students = StudentRegistration.objects.all()
        classes = Class.objects.all()  # Assuming you have a Class model for class levels
        context = {
            "students": students,
            # "classes": classes,
            "title": "Promote Students",
        }
        return render(request, "admin/promote_students.html", context)
    

    def get_extra_buttons(self):
        return [
            {
                'label': 'Promote Selected Students',
                'url': '/admin/admission/studentregistration/promote-students/',
                'class': 'button',  # You can add your own class for styling
                'icon': 'fas fa-arrow-up',  # Font Awesome icon if you're using them
            },
        ]
    



######################################################################################################################################################

    




class StudentRegistrationProxy(StudentRegistrationAdmin):
    class Meta:
        proxy = True
        verbose_name = "Student Registration Clone"
        verbose_name_plural = "Student Registration Clones"

admin.site.register(StudentRegistration, StudentRegistrationAdmin)




from django.contrib import admin
 # Import your filter class
from django_filters import FilterSet

class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'student_class', 'class_stream')  # Customize this as needed
    list_filter = (StudentFilter,)  # Add your filter class here

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset

# systemUsers/admin.py
from django.contrib import admin
from django.contrib import messages
from .models import ImportStudent, StudentRegistration
from .utils import import_students_from_file

# @admin.register(ImportStudent)
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

from .models import AcademicYear

class AcademicYearFilter(admin.SimpleListFilter):
    title = 'Academic Year'
    parameter_name = 'academic_year'

    def lookups(self, request, model_admin):
        return [(year.id, year.name) for year in AcademicYear.objects.all()]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(academic_year_id=self.value())
        return queryset
    
from .models import Term

class TermFilter(admin.SimpleListFilter):
    title = 'Term'
    parameter_name = 'term'

    def lookups(self, request, model_admin):
        return [(term.id, term.name) for term in Term.objects.all()]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(term_id=self.value())
        return queryset


# class UpgradeStudentAdminForm(forms.ModelForm):
#     class Meta:
#         model = UpgradeStudent
#         fields = '__all__'

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         if 'student_class' in self.data:
#             try:
#                 class_id = int(self.data.get('student_class'))
#                 self.fields['class_stream'].queryset = Stream.objects.filter(class_id=class_id)
#             except (ValueError, TypeError):
#                 pass  # Invalid input or no class selected
#         elif self.instance.pk:
#             self.fields['class_stream'].queryset = self.instance.student_class.stream_set.all()





# admin.py
# admin.py
from django.contrib import admin
from .models import UpgradeStudent, StudentRegistration, Class, AcademicYear, Term, Programme, Stream  # Import necessary models

class UpgradeStudentAdmin(admin.ModelAdmin):

    def has_add_permission(self, request):
        return False
    
    change_list_template = "admin/upgrade_students.html"  

    def changelist_view(self, request, extra_context=None):

        academic_year = AcademicYear.objects.all()
        term = Term.objects.all()
        programmes = Programme.objects.all()
        classes = Class.objects.all()
        stream = Stream.objects.all()
        students = StudentRegistration.objects.all()
        
        extra_context = extra_context or {}
        extra_context.update({
            "academic_year": academic_year,
            "term": term,
            "programmes": programmes,
            "classes": classes,
            "stream": stream,
            "students": students,
            "title": "Upgrade Based the following Criterials ",
        })
        
        return super().changelist_view(request, extra_context=extra_context)

# admin.site.register(UpgradeStudent, UpgradeStudentAdmin)


from django.contrib import admin
from .models import StudentRegistrationProxy



class AcademicYearFilter(admin.SimpleListFilter):
    title = 'Academic Year'
    parameter_name = 'academic_year'

    def lookups(self, request, model_admin):
        return [(year.id, year.name) for year in AcademicYear.objects.all()]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(entry_year__id=self.value())
        return queryset
    
class ProgrammeFilter(admin.SimpleListFilter):
    title = 'Programme'
    parameter_name = 'entry_programme'

    def lookups(self, request, model_admin):
        return [(programme.id, programme.name) for programme in Programme.objects.all()]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(entry_programme_id__in=self.value().split(','))
        return queryset
    
class TermFilter(admin.SimpleListFilter):
    title = 'Term'
    parameter_name = 'term'

    def lookups(self, request, model_admin):
        return [(term.id, term.name) for term in Term.objects.all()]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(entry_term__id=self.value())
        return queryset

class ClassFilter(admin.SimpleListFilter):
    title = 'Class'
    parameter_name = 'class'

    def lookups(self, request, model_admin):
        return [(cls.id, cls.class_name) for cls in Class.objects.all()]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(entry_class__id=self.value())
        return queryset

class StreamFilter(admin.SimpleListFilter):
    title = 'Stream'
    parameter_name = 'stream'

    def lookups(self, request, model_admin):
        return [(stream.id, stream.name) for stream in Stream.objects.all()]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(stream_name__id=self.value())
        return queryset

class SubjectFilter(admin.SimpleListFilter):
    title = 'Subject'
    parameter_name = 'subject'

    def lookups(self, request, model_admin):
        # Assuming that the `Subject` model has a `name` field for subject names
        return [(subject.id, subject.subject_name) for subject in Subject.objects.all()]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(subjects__id=self.value())  # Assuming `subjects` is the ManyToMany field
        return queryset



class ClassFilter(admin.SimpleListFilter):
    title = 'Class'
    parameter_name = 'entry_class'

    def lookups(self, request, model_admin):
        return [(cls.id, cls.class_name) for cls in Class.objects.all()]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(entry_class_id__in=self.value().split(','))
        return queryset


class StreamFilter(admin.SimpleListFilter):
    title = 'Stream'
    parameter_name = 'class_stream'

    def lookups(self, request, model_admin):
        return [(stream.id, stream.name) for stream in Stream.objects.all()]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(entry_stream__in=self.value().split(','))
        return queryset
    

from .models import Class

class StudentClassFilter(admin.SimpleListFilter):
    title = 'Student Class'
    parameter_name = 'student_class'

    def lookups(self, request, model_admin):
        return [(cls.id, cls.class_name) for cls in Class.objects.all()]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(student_class_id=self.value())
        return queryset


from .models import Stream

class ClassStreamFilter(admin.SimpleListFilter):
    title = 'Class Stream'
    parameter_name = 'class_stream'

    def lookups(self, request, model_admin):
        return [(stream.id, stream.name) for stream in Stream.objects.all()]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(stream_name_id=self.value())
        return queryset 



########################################################################################


from django.shortcuts import render
from django.contrib import admin
from .models import StudentRegistrationProxy  # Adjust import based on your models

from django.shortcuts import render
from django.urls import path
from django.http import HttpResponseRedirect

from django.shortcuts import render
from django.contrib import admin
from .models import StudentRegistrationProxy  # Adjust import based on your models

from django.shortcuts import render
from django.contrib import admin
from .models import StudentRegistrationProxy  # Adjust import based on your models

from django.contrib import admin
from .models import StudentRegistrationProxy  # Adjust import based on your models

from django.contrib import admin
from django.shortcuts import render
from .models import StudentRegistrationProxy, AcademicYear, Programme, Term, Class, Stream  # Adjust imports as necessary

class StudentRegistrationProxyAdmin(admin.ModelAdmin):
    list_display = ('registration_number', 'first_name', 'last_name')
    list_filter = (AcademicYearFilter, ProgrammeFilter, TermFilter, ClassFilter, ClassStreamFilter)
    search_fields = ('registration_number', 'first_name', 'last_name')

    change_list_template = "admin/upgradestudents.html"  # Use custom template

    actions = ['update_students']

    def changelist_view(self, request, extra_context=None):
        # Fetch filter options
        academic_years = AcademicYear.objects.all()
        programmes = Programme.objects.all()
        terms = Term.objects.all()
        classes = Class.objects.all()
        streams = Stream.objects.all()

        # Initialize the extra context
        extra_context = {
            'academic_years': academic_years,
            'programmes': programmes,
            'terms': terms,
            'classes': classes,
            'streams': streams,
        }

        filtered_students = StudentRegistration.objects.all()  # Default to all students

        if request.method == 'POST':
            academic_year = request.POST.get('academic_year')
            programme = request.POST.get('programme')
            term = request.POST.get('term')
            class_filter = request.POST.get('class')
            stream_filter = request.POST.get('stream')

            # Filter students based on the selected criteria
            if academic_year:
                filtered_students = filtered_students.filter(entry_year_id=academic_year)
            if programme:
                filtered_students = filtered_students.filter(entry_programme_id=programme)
            if term:
                filtered_students = filtered_students.filter(entry_term_id=term)
            if class_filter:
                filtered_students = filtered_students.filter(entry_class_id=class_filter)
            if stream_filter:
                filtered_students = filtered_students.filter(stream_name_id=stream_filter)

            # Check if any students were found
            if not filtered_students.exists():
                extra_context['error_message'] = "No students found matching the criteria."
            else:
                extra_context['filtered_students'] = filtered_students

        return super().changelist_view(request, extra_context=extra_context)

    def update_students(self, request, queryset):
        if request.method == 'POST':
            student_ids = request.POST.getlist('student_ids')  # Get the list of selected student IDs
            academic_year = request.POST.get('academic_year_new')
            programme = request.POST.get('programme_new')
            term = request.POST.get('term_new')
            class_filter = request.POST.get('class_new')
            stream_filter = request.POST.get('stream_new')
            
            print(academic_year,programme,term,class_filter,stream_filter)

        # Update each selected student
        for student_id in student_ids:
            student = StudentRegistrationProxy.objects.get(id=student_id)
            if academic_year:
                student.entry_year_id = academic_year
            if programme:
                student.entry_programme_id = programme
            if term:
                student.entry_term_id = term
            if class_filter:
                student.entry_class_id = class_filter
            if stream_filter:
                student.stream_name_id = stream_filter
            student.save()

        self.message_user(request, "Selected students have been updated.")
        return None  # Redirect to the same page

    # Display the form for updating the students (as shown in previous steps)
    # ...

        # # Display a form for updating the students
        # academic_years = AcademicYear.objects.all()
        # programmes = Programme.objects.all()
        # terms = Term.objects.all()
        # classes = Class.objects.all()
        # streams = Stream.objects.all()

        # context = {
        #     'academic_years': academic_years,
        #     'programmes': programmes,
        #     'terms': terms,
        #     'classes': classes,
        #     'streams': streams,
        #     'students': queryset,
        # }

        # return render(request, 'admin/update_students.html', context)

# Register the proxy model and admin class
admin.site.register(StudentRegistrationProxy, StudentRegistrationProxyAdmin)






    # def upgrade_students(self, request, queryset):
    #     student_ids = request.POST.getlist('_selected_action')
    #     selected_students = queryset.filter(id__in=student_ids)

    #     # Get filter values from the request
    #     academic_year = request.GET.get('academic_year', None)
    #     programme = request.GET.get('programme', None)
    #     term = request.GET.get('term', None)
    #     class_filter = request.GET.get('class', None)
    #     class_stream = request.GET.get('class_stream', None)

    #     context = {
    #         'academic_year': academic_year,
    #         'programme': programme,
    #         'term': term,
    #         'class_filter': class_filter,
    #         'class_stream': class_stream,
    #         'selected_students': selected_students,
    #         'request': request,  # Pass the request
    #     }
        
        # return render(request, 'admin/upgradestudents.html', context)
    
    #  change_list_template = "admin/upgrade_students.html"  
    

#     def changelist_view(self, request, extra_context=None):
#         return super().changelist_view(request, extra_context=extra_context)

# # Register the proxy model and admin class
# admin.site.register(StudentRegistrationProxy, StudentRegistrationProxyAdmin)



    #  def custom_report_button(self, obj):
    #     url = reverse('admin:custom_report')
    #     return format_html('<a class="button" href="{}">View Custom Report</a>', url)
    
    # custom_report_button.short_description = "Custom Report"  # Button label
    # custom_report_button.allow_tags = True

    # # Display button in the model’s detail view
    # readonly_fields = ("custom_report_button",)





    # # Define the action for promoting students
    # def promote_selected_students(self, request, queryset):
    #     selected_ids = queryset.values_list('id', flat=True)
    #     request.session['selected_student_ids'] = list(selected_ids)
    #     return redirect('admin:promote-students')  # Redirect to custom page

    # promote_selected_students.short_description = "Promote selected students"

    # # Define URLs for the custom admin actions
    # def get_urls(self):
    #     urls = super().get_urls()
    #     custom_urls = [
    #         path('promote-students/', self.admin_site.admin_view(self.promote_students), name='promote-students'),
    #     ]
    #     return custom_urls + urls
    
    
# from django.contrib import admin
# from .models import RoomAllocation

# class RoomAllocationAdmin(admin.ModelAdmin):
#     list_display = ('student_name', 'room_name', 'room_number')
#     search_fields = ('student_name__first_name', 'student_name__last_name', 'room_name', 'room_number')
#     list_filter = ('room_name',)

# admin.site.register(RoomAllocation, RoomAllocationAdmin)





from django.contrib import admin
from .models import RoomAllocation, SetRoom

@admin.register(RoomAllocation)
class RoomAllocationAdmin(admin.ModelAdmin):
    list_display = ('student', 'allocated_dormitory', 'remaining_capacity_display', 'allocation_date')
    search_fields = ('student__first_name', 'student__last_name', 'allocated_dormitory__dormitory_name')
    list_filter = ('allocated_dormitory',)

    def remaining_capacity_display(self, obj):
        return obj.remaining_capacity()
    remaining_capacity_display.short_description = 'Remaining Capacity'




from django.contrib import admin
from .models import SchoolContributions

class SchoolContributionsAdmin(admin.ModelAdmin):
    list_display = ('student_name', 'contribution_for', 'amount')
    search_fields = ('student_name__first_name', 'student_name__last_name', 'contribution_for')
    list_filter = ('contribution_for',)

admin.site.register(SchoolContributions, SchoolContributionsAdmin)


from django.contrib import admin
from .models import SetRoom

@admin.register(SetRoom)
class SetRoomAdmin(admin.ModelAdmin):
    list_display = ('dormitory_name', 'capacity')
    search_fields = ('dormitory_name',)
    list_filter = ('capacity',)


from django.contrib import admin
from .models import SetSponsor

# @admin.register(SetSponsor)
# class SetSponsorAdmin(admin.ModelAdmin):
#     list_display = ('sponsor_name',)
#     search_fields = ('sponsor_name',)



from django.contrib import admin
from .models import SetSponsor, Sponsor

class SponsorAdmin(admin.ModelAdmin):
    list_display = ('sponsor_name', 'mobile', 'email', 'postal_address', 'physical_address')
    search_fields = ('sponsor_name__sponsor_name',)

    class Media:
        js = ('js/sponsor_admin.js',)  # Ensure you have this JavaScript file

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        # Customize the queryset for the sponsor_name field if needed
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

admin.site.register(Sponsor, SponsorAdmin)
    