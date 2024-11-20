from django.contrib import admin
from results.models import ExaminationResult, Result, ResultSummary
from Record_results.models import QueResults
from exam_setting.models import GradeDivision, GradeScale
from .models import Department, SubjectConfig

class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name',)  # Display the name field in the list view
    search_fields = ('name',)  # Allow searching by name
    ordering = ('name',)  # Order the list by name

admin.site.register(Department, DepartmentAdmin)

from .models import Programme

class ProgramAdmin(admin.ModelAdmin):
    list_display = ('name',)  # Display the name field in the list view
    search_fields = ('name',)  # Allow searching by name
    ordering = ('name',)  # Order the list by name

admin.site.register(Programme, ProgramAdmin)

from .models import Subject
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('subject_code', 'subject_name','status','department')  # Display relevant fields
    search_fields = ('subject_code', 'subject_name')  # Allow searching by subject code and name
    ordering = ('subject_name',)  # Order the list by subject name

admin.site.register(Subject, SubjectAdmin)

from .models import Class

class ClassAdmin(admin.ModelAdmin):
    list_display = ('programme', 'class_name', 'no_of_stream', 'view_assigned_streams')
    filter_horizontal = ('assigned_streams',)  # Enables a user-friendly interface for selecting streams

admin.site.register(Class, ClassAdmin)# Order the list by program and class names


from .models import Term

class TermAdmin(admin.ModelAdmin):
    list_display = ('name',)  # Display the name field in the list view
    search_fields = ('name',)  # Allow searching by term name
    ordering = ('name',)  # Order the list by term name

# Register the Term model with the admin site
admin.site.register(Term, TermAdmin)

from .models import AcademicYear

class AcademicYearAdmin(admin.ModelAdmin):
    list_display = ('name', 'status')  # Display name and status in the list view
    search_fields = ('name',)  # Allow searching by name
    ordering = ('name',)  # Order by name

# Register the AcademicYear model with the admin site
admin.site.register(AcademicYear, AcademicYearAdmin)

from .models import Assessment

class AssessmentAdmin(admin.ModelAdmin):
    list_display = ('name',)  # Display the name field in the list view
    search_fields = ('name',)  # Allow searching by name
    ordering = ('name',)  # Order by name

# Register the Assessment model with the admin site
admin.site.register(Assessment, AssessmentAdmin)

from django.contrib import admin
from .models import Stream

@admin.register(Stream)
class StreamAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)



class SubjectConfigAdmin(admin.ModelAdmin):
    list_display = ('class_name', 'get_assigned_streams', 'no_of_assigned_subjects', 'get_subjects')
    search_fields = ('class_name__class_name',)  # Search by class name
    filter_horizontal = ('assigned_streams', 'subjects')

    def get_assigned_streams(self, obj):
        return ", ".join([stream.name for stream in obj.assigned_streams.all()])
    get_assigned_streams.short_description = 'Assigned Streams'  # Name displayed in the admin

    def get_subjects(self, obj):
        return ", ".join([subject.subject_name for subject in obj.subjects.all()])
    get_subjects.short_description = 'Subjects'  # Name displayed in the admin

admin.site.register(SubjectConfig, SubjectConfigAdmin)



# systemUsers/admin.py
from django.contrib import admin
from .models import SubjectAllocation

class SubjectAllocationAdmin(admin.ModelAdmin):
    list_display = (
        'academic_year', 
        'term', 
        'subject', 
        'class_name', 
        'teacher_full_name',  # Display teacher's full name
        'phone_number',       # Display teacher's phone number
        'assigned_date', 
        'status'
    )
    search_fields = (
        'subject__name', 
        'class_name__class_name', 
        'teacher__full_name', 
        'phone_number'
    )
    
    # Method to display teacher's full name in the admin list view
    @admin.display(description='Full Name')
    def teacher_full_name(self, obj):
        return obj.teacher.first_name
    
    # Method to display teacher's phone number in the admin list view
    @admin.display(description='Phone Number')
    def phone_number(self, obj):
        return obj.teacher.phone_number

admin.site.register(SubjectAllocation, SubjectAllocationAdmin)


# systemUsers/admin.py
from django.contrib import admin
from .models import ResultsDeadline  # Import ResultsDeadline model

class ResultsDeadlineAdmin(admin.ModelAdmin):
    list_display = ('program_name', 'deadline_date')
    search_fields = ('program_name__name',)  # Assuming Programme model has a 'name' field

admin.site.register(ResultsDeadline, ResultsDeadlineAdmin)

# systemUsers/admin.py
from django.contrib import admin
# from .models import Publish  # Import Publish model

# class PublishAdmin(admin.ModelAdmin):
#     list_display = ('program_name', 'action')
#     list_filter = ('action',)
#     search_fields = ('program_name__name',)  # Assuming Programme model has a 'name' field

# admin.site.register(Publish, PublishAdmin)



from django.urls import path
from django.shortcuts import redirect
from django.utils.html import format_html
from django.contrib import messages
from django.contrib import admin, messages
from django.urls import path
from django.shortcuts import render, redirect
from admission.admin import AcademicYearFilter, ClassFilter, ProgrammeFilter, StreamFilter, TermFilter
from admission.models import StudentRegistration



class StudentRegistrationAdmin(admin.ModelAdmin):
    list_display = ('registration_number', 'first_name', 'last_name', 'entry_year', 'entry_programme', 'entry_class', 'custom_actions')
    list_filter = (AcademicYearFilter, TermFilter, ProgrammeFilter, ClassFilter, StreamFilter)
    search_fields = ('registration_number', 'first_name', 'last_name')  
    actions = ['promote_students_action','add_results'] 
    
    # Define the action for promoting students
    def promote_selected_students(self, request, queryset):
        selected_ids = queryset.values_list('id', flat=True)
        request.session['selected_student_ids'] = list(selected_ids)
        return redirect('admin:promote-students')  # Redirect to custom page

    promote_selected_students.short_description = "Promote selected students"

    # Define URLs for the custom admin actions
    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('promote-students/', self.admin_site.admin_view(self.promote_students), name='promote-students'),
        ]
        return custom_urls + urls

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
                'classes': Class.objects.all(),
            }
            return render(request, 'admin/promote_students.html', context)
        
    def custom_actions(self, obj):
        return format_html(
                 '<a class="button" href="{}">Promote Students</a>',
                 "promote-students/"
        )
    custom_actions.short_description = 'Actions'
    
    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('promote/<int:student_id>/', self.admin_site.admin_view(self.promote_student), name="promote-student"),
            path('send-reminder/<int:student_id>/', self.admin_site.admin_view(self.send_reminder), name="send-reminder"),
        ]
        return custom_urls + urls

    def promote_student(self, request, student_id):
        # Implement the logic to promote a student here
        messages.success(request, f"Student {student_id} promoted successfully.")
        return redirect("..")

    def send_reminder(self, request, student_id):
        # Implement the logic to send a reminder here
        messages.success(request, f"Reminder sent to student {student_id}.")
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
            "classes": classes,
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
    
    

from .models import Publish
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.utils import timezone
from django.contrib import messages
from .models import Publish
from django.utils import timezone
from django.contrib import messages
from django.db import transaction
from django.db import IntegrityError
from django.db import models
from django.db.models import Count, Q


from django.contrib import admin
from django.db import models
from django.db.models import Count, Q
from decimal import Decimal, InvalidOperation
from collections import defaultdict
from django.db import models



############################################################################################################################################

class PublishAdmin(admin.ModelAdmin):
    list_display = ('program_name',)
    actions = ['publish_selected', 'unpublish_selected'] 
    
    def publish_selected(self, request, queryset):
        division_counts = defaultdict(int)
        que_results = QueResults.objects.values('academic_year', 'term', 'exam_type', 'registration_number', 'student_name', 'result', 'result_summary')
        for que_result in que_results:
            aggregated_results = QueResults.objects.filter(
            academic_year=que_result['academic_year'],
            term=que_result['term'],
            exam_type=que_result['exam_type'],
            registration_number=que_result['registration_number'],
            student_name=que_result['student_name']
        ).aggregate(
            total=models.Sum('result'),
            average=models.Avg('result')
        )
        
        total_result = aggregated_results['total'] 
        average_result = aggregated_results['average'] 
        
        # Determine grade and division
        grade_instance = GradeScale.objects.filter(minimum_marks__lte=average_result).order_by('-minimum_marks').first()
        grade_name = grade_instance.grade_name if grade_instance else None
        grade_point = grade_instance.grade_point if grade_instance else None
        
        division_instance = GradeDivision.objects.filter(minimum_division_point__lte=average_result).order_by('-minimum_division_point').first()
        division_title = division_instance.division_title if division_instance else None
        
        # Count the division title
        if division_title in ['I', 'II', 'III', 'IV', '0', 'INC', 'ABS']:
            division_counts[division_title] += 1
        
        # Update or create Result instance
        existing_result = Result.objects.filter(
            academic_year=que_result['academic_year'],
            term=que_result['term'],
            registration_number=que_result['registration_number'],
            full_name=que_result['student_name']
        ).first() 
        
        if existing_result: 
            existing_result.subject += f", {que_result['result_summary']}"  
            existing_result.total = total_result 
            existing_result.avg = average_result
            existing_result.grade = grade_name  # Update the grade
            existing_result.point = grade_point  # Update the grade point
            existing_result.division = division_title
            existing_result.save() 
        else:
            Result.objects.create(
                academic_year=que_result['academic_year'],
                term=que_result['term'],
                exam_type=que_result['exam_type'],
                registration_number=que_result['registration_number'],
                full_name=que_result['student_name'],
                subject=que_result['result_summary'],
                total=total_result,
                avg=average_result,  
                grade=grade_name,  # Update the grade
                point=grade_point,
                division=division_title
            )
            
            result_summary, created = ResultSummary.objects.get_or_create(
                academic_year=que_result['academic_year'],
                term=que_result['term'],
                registration_number=que_result['registration_number'],
            )


            result_summary.grade_I += division_counts['I']
            result_summary.grade_II += division_counts['II']
            result_summary.grade_III += division_counts['III']
            result_summary.grade_IV += division_counts['IV']
            result_summary.grade_0 += division_counts['0']
            result_summary.incomplete += division_counts['INC']
            result_summary.absent += division_counts['ABS']
            result_summary.save()
            
            self.message_user(request, "Results Published Successfully.")
          
         
admin.site.register(Publish, PublishAdmin)





# class PublishAdmin(admin.ModelAdmin):
#     list_display = ('program_name',)
#     actions = ['publish_selected', 'unpublish_selected']  # Add custom actions
    
# def publish_selected(self, request, queryset):
#     publish_selected.short_description = "Publish selected Exam"

#     que_results = QueResults.objects.values(
#         'academic_year', 'term', 'exam_type', 'registration_number', 'student_name', 'result', 'result_summary'
#     )
    
#     for que_result in que_results:
#         # Aggregate total and average results
#         aggregated_results = QueResults.objects.filter(
#             academic_year=que_result['academic_year'],
#             term=que_result['term'],
#             exam_type=que_result['exam_type'],
#             registration_number=que_result['registration_number'],
#             student_name=que_result['student_name']
#         ).aggregate(
#             total=models.Sum('result'),
#             average=models.Avg('result')
#         )
        
#         total_result = aggregated_results['total']
#         average_result = aggregated_results['average']
        
#         # Determine grade and division
#         grade_instance = GradeScale.objects.filter(
#             minimum_marks__lte=average_result
#         ).order_by('-minimum_marks').first()
        
#         grade_name = grade_instance.grade_name if grade_instance else None
#         grade_point = grade_instance.grade_point if grade_instance else None
        
#         division_instance = GradeDivision.objects.filter(
#             minimum_division_point__lte=average_result
#         ).order_by('-minimum_division_point').first()
        
#         division_title = division_instance.division_title if division_instance else None
        
#         # Update or create Result entry
#         existing_result = Result.objects.filter(
#             academic_year=que_result['academic_year'],
#             term=que_result['term'],
#             registration_number=que_result['registration_number'],
#             full_name=que_result['student_name']
#         ).first()
        
#         if existing_result:
#             existing_result.subject += f", {que_result['result_summary']}"
#             existing_result.total = total_result
#             existing_result.avg = average_result
#             existing_result.grade = grade_name
#             existing_result.point = grade_point
#             existing_result.division = division_title
#             existing_result.save()
#         else:
#             Result.objects.create(
#                 academic_year=que_result['academic_year'],
#                 term=que_result['term'],
#                 exam_type=que_result['exam_type'],
#                 registration_number=que_result['registration_number'],
#                 full_name=que_result['student_name'],
#                 subject=que_result['result_summary'],
#                 total=total_result,
#                 avg=average_result,
#                 grade=grade_name,
#                 point=grade_point,
#                 division=division_title
#             )
        
#         # Count each division title for the academic year, term, and exam type
#         division_counts = Result.objects.filter(
#             academic_year=que_result['academic_year'],
#             term=que_result['term'],
#             exam_type=que_result['exam_type']
#         ).aggregate(
#             grade_I=Count('division', filter=Q(division="I")),
#             grade_II=Count('division', filter=Q(division="II")),
#             grade_III=Count('division', filter=Q(division="III")),
#             grade_IV=Count('division', filter=Q(division="IV")),
#             grade_0=Count('division', filter=Q(division="0")),
#             incomplete=Count('division', filter=Q(division="INC")),
#             absent=Count('division', filter=Q(division="ABS"))
#         )
        
#         # Update or create the ResultSummary record
#         ResultSummary.objects.update_or_create(
#             academic_year=que_result['academic_year'],
#             term=que_result['term'],
#             exam_type=que_result['exam_type'],
#             registration_number=que_result['registration_number'],
#             defaults={
#                 'grade_I': division_counts['grade_I'],
#                 'grade_II': division_counts['grade_II'],
#                 'grade_III': division_counts['grade_III'],
#                 'grade_IV': division_counts['grade_IV'],
#                 'grade_0': division_counts['grade_0'],
#                 'incomplete': division_counts['incomplete'],
#                 'absent': division_counts['absent']
#             }
#         )
        

        
#     self.message_user(request, f" Results Published Successfully.")
          
       


    # def unpublish_selected(self, request, queryset):
    #     """Action to unpublish selected items."""
    #     updated_count = queryset.update(action='unpublish', published_date=None, published_by=None)
    #     messages.success(request, f"{updated_count} program(s) were successfully unpublished.")

    #     unpublish_selected.short_description = "Unpublish selected items"

# admin.site.register(Publish, PublishAdmin)



from django.contrib import admin
from .models import Contact

class ContactAdmin(admin.ModelAdmin):
    list_display = ('phone_number', 'email', 'address')
    search_fields = ('email', 'phone_number', 'address')

admin.site.register(Contact, ContactAdmin)


from django.contrib import admin
from .models import Teacher

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'phone_number', 'username')
    search_fields = ('first_name', 'last_name', 'username', 'phone_number')

