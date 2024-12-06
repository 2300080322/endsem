from django import forms
from .models import NewFeature
from .models import Certification, Assignment, Progress
class NewFeatureForm(forms.ModelForm):
    class Meta:
        model = NewFeature
        fields = ['title', 'description']

class CertificationForm(forms.ModelForm):
    class Meta:
        model = Certification
        fields = ['employee', 'course', 'date_completed']

class AssignmentForm(forms.ModelForm):
    class Meta:
        model = Assignment
        fields = ['employee', 'course', 'title', 'due_date', 'status']

class ProgressForm(forms.ModelForm):
    class Meta:
        model = Progress
        fields = ['employee', 'course', 'progress_percent']