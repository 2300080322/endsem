from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Course, Student, Enrollment, AddCourse
from .forms import CourseForm, AddCourseForm

# Trainer homepage
def trainerhomepagecall(request):
    courses = Course.objects.all()  # Retrieve all courses
    return render(request, 'trainerapp/trainerhomepage.html', {'courses': courses})

# Add a new course with predefined options
def add_course(request):
    if request.method == 'POST':
        form = AddCourseForm(request.POST)
        if form.is_valid():
            form.save()  # Save the AddCourse instance to the database
            return redirect('trainerapp:course_list')  # Redirect to the course list page
    else:
        form = AddCourseForm()  # Create an empty form for GET request

    return render(request, 'trainerapp/add_course.html', {'form': form})

# List all courses
def course_list(request):
    courses = Course.objects.all()  # Fetch all courses from the database
    return render(request, 'trainerapp/course_list.html', {'courses': courses})

# Show course details
def course_detail(request, pk):
    course = get_object_or_404(Course, pk=pk)  # Fetch the course by its primary key
    return render(request, 'trainerapp/course_detail.html', {'course': course})

# Enroll a student in a course
def enroll_student(request, course_id):
    course = get_object_or_404(Course, id=course_id)  # Fetch the course by its ID
    students = Student.objects.exclude(enrollments__course=course)  # Students not already enrolled

    if request.method == 'POST':
        student_id = request.POST.get('student_id')
        try:
            student = get_object_or_404(Student, id=student_id)  # Fetch the student by their ID
            Enrollment.objects.create(student=student, course=course)  # Create an enrollment
            return HttpResponseRedirect(reverse('trainerapp:course_detail', args=[course.id]))
        except Exception as e:
            # Handle errors, such as invalid student ID
            return render(request, 'trainerapp/enroll_student.html', {
                'course': course,
                'students': students,
                'error': str(e)
            })

    return render(request, 'trainerapp/enroll_student.html', {'course': course, 'students': students})

# Default enroll student view
def enroll_student_default(request):
    return HttpResponse("Enroll Student Default View")
