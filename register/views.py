from django.db import IntegrityError
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.decorators import login_required
from events.models import Events

def register(request):
    if request.method=='POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        confirmpassword=request.POST.get('confirmpassword')

        if password==confirmpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username already taken")
                return redirect('register/')
            
            elif User.objects.filter(email=email).exists():
                messages.info(request,"Email id already taken")
                return redirect('register/')
            
            else:
                user_reg=User.objects.create_user(username=username, email=email, password=password)
                user_reg.save()
                messages.info(request,"Successfully Created")
                return redirect('/')
        else:
            messages.info(request,"Password doesnot Match")

            return redirect('register/')


    return render(request,'register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, "Login successful")
            if user.is_superuser:
                return redirect('admin_dashboard')  # Redirect superuser to admin dashboard
            else:
                return redirect('user_dashboard')  # Redirect normal user to user dashboard
        else:
            messages.error(request, "Invalid username or password")
            return redirect('login')

    return render(request, 'login.html')


@login_required
def logout(request):
    auth.logout(request)
    messages.success(request, "You have been logged out.")
    return redirect('/')

def admin_dashboard(request):
    # Ensure only superusers can access this view
    if not request.user.is_superuser:
        return redirect('login')
    return render(request, 'admin_dashboard.html')

def user_dashboard(request):
    
    events = Events.objects.all()  # or filter based on the user's interests
    context = {
        'events': events,
    }
    return render(request, 'user_dashboard.html')