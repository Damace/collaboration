# custom_user/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import CustomUserLoginForm, StudentLoginForm
from .models import Student

def custom_user_login(request):
    if request.method == 'POST':
        form = CustomUserLoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')  # Adjust to your desired redirect
    else:
        form = CustomUserLoginForm()
    return render(request, 'registration/user_login.html', {'form': form})

def student_login(request):
    if request.method == 'POST':
        form = StudentLoginForm(request.POST)
        if form.is_valid():
            registration_number = form.cleaned_data['registration_number']
            password = form.cleaned_data['password']
            try:
                student = Student.objects.get(registration_number=registration_number)
                if student.password == password:  # Ideally, use hashed passwords
                    # Log the student in (set session or similar)
                    request.session['student_id'] = student.id
                    return redirect('student_home')  # Adjust to your desired redirect
            except Student.DoesNotExist:
                form.add_error(None, "Invalid registration number or password.")
    else:
        form = StudentLoginForm()
    return render(request, 'registration/student_login.html', {'form': form})