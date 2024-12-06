from django.db import models
from django.contrib.auth.models import User

class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    duration = models.IntegerField(help_text="Duration in hours or days, depending on your app logic")

    def __str__(self):
        return self.title

class Trainer(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='student_profile')
    courses = models.ManyToManyField(Course, through='Enrollment', related_name='enrolled_students')

    def __str__(self):
        return self.user.username

class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='enrollments')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='enrollments')
    enrolled_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('student', 'course')  # Prevent duplicate enrollments
        ordering = ['-enrolled_at']  # Recent enrollments first

    def __str__(self):
        return f'{self.student.user.username} enrolled in {self.course.title}'

class AddCourse(models.Model):
    COURSE_CHOICES = [
        ('AOOP', 'ADVANCED OBJECT ORIENTED PROGRAMMING'),
        ('PFSD', 'PYTHON FULL STACK DEVELOPMENT'),
    ]
    SECTION_CHOICES = [
        ('S11', 'SECTION S11'),
        ('S12', 'SECTION S12'),
        ('S13', 'SECTION S13'),
        ('S14', 'SECTION S14'),
        ('S15', 'SECTION S15'),
        ('S16', 'SECTION S16'),
        ('S17', 'SECTION S17'),
    ]

    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.CharField(max_length=50, choices=COURSE_CHOICES)
    section = models.CharField(max_length=50, choices=SECTION_CHOICES)

    def __str__(self):
        return f'{self.student.user.username} - {self.course} ({self.section})'
