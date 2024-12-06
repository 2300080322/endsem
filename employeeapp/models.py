from django.db import models
from django.contrib.auth.models import User

class EmployeeProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, default='Unknown')
    last_name = models.CharField(max_length=100)
    email = models.EmailField(default='default@example.com')  # This can be removed if you're using user.email
    phone = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    skills = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"

    class Meta:
        verbose_name = "Employee Profile"
        verbose_name_plural = "Employee Profiles"


class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    assigned_to = models.ForeignKey(EmployeeProfile, on_delete=models.CASCADE, related_name='tasks')
    due_date = models.DateField()
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['due_date']  # Default ordering by due date


class NewFeature(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)  # Optional field to track creation time

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "New Feature"
        verbose_name_plural = "New Features"

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()

class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    duration = models.PositiveIntegerField(help_text="Duration in hours")

class Certification(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date_completed = models.DateField()

class Assignment(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    due_date = models.DateField()
    status = models.CharField(max_length=50, choices=[('Pending', 'Pending'), ('Completed', 'Completed')])

class Progress(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    progress_percent = models.FloatField()



