# # systemUsers/management/commands/create_user.py
# from django.core.management.base import BaseCommand
# from systemUsers.models import CustomUser

# class Command(BaseCommand):
#     help = 'Create a user'

#     def handle(self, *args, **kwargs):
#         user = CustomUser.objects.create_user(
#             username='testuser',
#             email='test@example.com',
#             password='testpassword',
#             first_name='Test',
#             last_name='User',
#             role='Student'  # or any other role
#         )
#         user.is_staff = True  # Allow this user to access the admin site
#         user.save()
#         self.stdout.write(self.style.SUCCESS('User created successfully!'))


# systemUsers/management/commands/update_teacher_profile.py
from django.core.management.base import BaseCommand
from systemUsers.models import TeacherProfile, CustomUser

class Command(BaseCommand):
    help = 'Update the username of the second TeacherProfile object based on the associated CustomUser username'

    def handle(self, *args, **kwargs):
        # Fetch all TeacherProfile objects
        teacher_profiles = TeacherProfile.objects.all()

        # Check if there are at least two profiles
        if len(teacher_profiles) >= 2:
            # Get the second profile
            teacher_profile_to_update = teacher_profiles[1]  # Index 1 for the second object
            
            # Fetch the associated CustomUser
            user = teacher_profile_to_update.user  # Assuming `user` is the ForeignKey field in TeacherProfile
            
            # Update the username with the CustomUser's username
            teacher_profile_to_update.username = user.username  # Set to the associated CustomUser's username
            
            # Save the changes
            teacher_profile_to_update.save()

            self.stdout.write(self.style.SUCCESS(f'TeacherProfile updated to username: {teacher_profile_to_update.username}'))
        else:
            self.stdout.write(self.style.WARNING('There are less than 2 TeacherProfile objects.'))
