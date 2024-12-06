from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Task, EmployeeProfile
from .forms import NewFeatureForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login


# View for the Employee Homepage
def employeehomepagecall(request):
    return render(request, 'employeeapp/employeehomepage.html')


# View for Task List, which is protected by login_required decorator
@login_required
def task_list(request):
    try:
        employee_profile = request.user.employeeprofile
    except AttributeError:
        return redirect('some_error_page')  # Redirect to error page if profile does not exist

    # Retrieve tasks associated with the employee profile
    tasks = employee_profile.tasks.all()
    return render(request, 'employeeapp/tasks.html', {'tasks': tasks})


# View to add a new feature (based on NewFeatureForm)
@login_required
def add_new_feature(request):
    if request.method == 'POST':
        form = NewFeatureForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employeeapp:task_list')  # Redirect to task list after saving the new feature
    else:
        form = NewFeatureForm()
    return render(request, 'employeeapp/new_feature_form.html', {'form': form})


# View to create or update the employee profile
@login_required
def create_or_update_profile(request):
    user = request.user
    profile, created = EmployeeProfile.objects.get_or_create(user=user)

    if request.method == 'POST':
        profile.first_name = request.POST.get('first_name')
        profile.last_name = request.POST.get('last_name')
        profile.email = request.POST.get('email')
        profile.phone = request.POST.get('phone')
        profile.address = request.POST.get('address')
        profile.skills = request.POST.get('skills')
        profile.save()
        messages.success(request, "Profile updated successfully!")
        return redirect('employeeapp:view_profile')

    return render(request, 'employeeapp/create_profile.html', {'profile': profile})


# View to display the profile of the logged-in employee
@login_required
def view_profile(request):
    profile = EmployeeProfile.objects.get(user=request.user)
    return render(request, 'employeeapp/view_profile.html', {'profile': profile})


# View for user login
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('employeeapp:task_list')  # Redirect to the task list after successful login
    else:
        form = AuthenticationForm()
    return render(request, 'employeeapp/login.html', {'form': form})

from django.shortcuts import render

# Define the view for the error page
def some_error_page(request):
    return render(request, 'employeeapp/error_page.html')  # You can change the template to match your design


# views.py
from django.shortcuts import render, get_object_or_404
from .models import Employee, Certification, Assignment, Progress
from .forms import CertificationForm, AssignmentForm, ProgressForm


def track_progress(request):
    # Fetch all employees and their progress data
    employees = Employee.objects.all()  # Assuming Employee model stores employees
    progress_data = Progress.objects.select_related('employee', 'course').all()  # Join with Employee and Course models

    # Pass the data to the template
    return render(request, 'employeeapp/track_progress.html', {
        'employees': employees,
        'progress_data': progress_data
    })
def report(request):
    certifications = Certification.objects.select_related('employee', 'course').order_by('-date_completed')
    assignments_pending = Assignment.objects.filter(status='Pending').select_related('employee', 'course')
    return render(request, 'employeeapp/report.html', {
        'certifications': certifications,
        'assignments_pending': assignments_pending,
    })
