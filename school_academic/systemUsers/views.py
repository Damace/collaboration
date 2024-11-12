from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm

def custom_admin_login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/admin/')  # Redirect to admin home page
            else:
                messages.error(request, 'Invalid username or password')
    else:
        form = AuthenticationForm()
    return render(request, 'custom_admin_login.html', {'form': form})



from django.contrib.auth import logout
from django.shortcuts import redirect

def custom_logout_view(request):
    if request.method == 'POST':
        logout(request)  # Log the user out
        return render(request, 'accounts/logout.html')  # Render your custom logout template
    return redirect('admin:index')  # Redirect if accessed via GET

from django.contrib.auth import logout
from django.shortcuts import redirect

def custom_logout(request):
    logout(request)
    return redirect('admin:index')  # Redirect to the login screen after logout
