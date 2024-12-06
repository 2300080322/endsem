from django import forms
from .models import Course, AddCourse

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['title', 'description', 'duration']  # Fields to be included in the form
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4, 'cols': 40}),  # Custom widget for description field
        }

class AddCourseForm(forms.ModelForm):
    class Meta:
        model = AddCourse
        fields = ['student', 'course', 'section']  # Fields to include student, course, and section
