# accounts/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from .forms import CustomLoginForm

class CustomLoginView(LoginView):
    form_class = CustomLoginForm
    template_name = 'accounts/login.html'

    def form_valid(self, form):
        login(self.request, form.get_user())
        return redirect('home')  # Change 'home' to your desired redirect URL