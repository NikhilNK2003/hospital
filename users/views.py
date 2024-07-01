from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import SignUpForm

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST, request.FILES)
        if form.is_valid():
            # Save the user and authenticate
            user = form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Registration successful. You are now logged in.')
                return redirect('dashboard')
            else:
                messages.error(request, 'Authentication failed. Please try again.')
        else:
            messages.error(request, 'There was an error with your registration. Please correct the errors below.')
    else:
        form = SignUpForm()
    
    return render(request, 'signup.html', {'form': form})

@login_required
def dashboard(request):
    if request.user.user_type == 'patient':
        return render(request, 'patient_dashboard.html')
    elif request.user.user_type == 'doctor':
        return render(request, 'doctor_dashboard.html')
    else:
        messages.error(request, 'You do not have permission to access this dashboard.')
        return redirect('home')
