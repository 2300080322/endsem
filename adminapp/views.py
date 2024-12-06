from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout as auth_logout
from django.db.models import Avg
from .models import Feedback
from .forms import FeedbackForm

# Homepage view
def homepagecall(request):
    return render(request, 'adminapp/projecthomepage.html')

# Login page view
def loginpagecall(request):
    return render(request, 'adminapp/LoginPage.html')

# Registration page view
def registerpagecall(request):
    return render(request, 'adminapp/Register.html')

# User registration logic
def UserRegisterLogic(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        pass1 = request.POST['password']
        pass2 = request.POST['password1']

        if pass1 == pass2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'OOPS! Username already taken.')
                return redirect('adminapp:registerpagecall')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'OOPS! Email already registered.')
                return redirect('adminapp:registerpagecall')
            else:
                user = User.objects.create_user(
                    username=username,
                    password=pass1,
                    first_name=first_name,
                    last_name=last_name,
                    email=email
                )
                user.save()
                messages.success(request, 'Account created successfully!')
                return redirect('adminapp:projecthomepage')
        else:
            messages.error(request, 'Passwords do not match.')
            return redirect('adminapp:registerpagecall')
    return render(request, 'adminapp/Register.html')
# User login logic
def UserLoginLogic(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if len(username) == 10:
                messages.success(request, 'Login successful as student!')
                return redirect('trainerapp:trainerhomepage')
            elif len(username) == 4:
                messages.success(request, 'Login successful as faculty!')
                return redirect('employeeapp:employeehomepage')
            else:
                messages.error(request, 'Username length does not match student or faculty criteria.')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'adminapp/LoginPage.html')

# Submit feedback logic
from django.shortcuts import render, redirect
from .forms import FeedbackForm

def submit_feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('adminapp:feedback_list')  # Ensure 'feedback_list' URL exists in the URLconf
    else:
        form = FeedbackForm()

    return render(request, 'adminapp/submit_feedback.html', {'form': form})

# Feedback list view
def feedback_list(request):
    feedbacks = Feedback.objects.all()
    print(feedbacks)
    return render(request, 'adminapp/feedback_list.html', {'feedbacks': feedbacks})

# Feedback success view
def feedback_success(request):
    feedbacks = Feedback.objects.all()  # Retrieve all feedback from the database
    return render(request, 'adminapp/feedback_success.html', {'feedbacks': feedbacks})
# Admin dashboard view
def admin_dashboard(request):
    # Fetch all feedbacks
    feedbacks = Feedback.objects.all().order_by('-created_at')

    # Calculate average rating (handle empty case)
    average_rating = feedbacks.aggregate(Avg('rating')).get('rating__avg')
    feedback_summary = {
        'average_rating': average_rating if average_rating else "No ratings available"
    }

    return render(request, 'adminapp/dashboard.html', {
        'feedbacks': feedbacks,
        'feedback_summary': feedback_summary
    })
# Logout logic
def logout(request):
    auth_logout(request)
    return redirect('adminapp:LoginPage')
