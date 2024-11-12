# custom_user/forms.py
from django import forms
from django.contrib.auth.forms import AuthenticationForm

class CustomUserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Username', max_length=254)

class StudentLoginForm(forms.Form):
    registration_number = forms.CharField(label='Registration Number', max_length=20)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)