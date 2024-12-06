from django.urls import path
from . import views

app_name = 'trainerapp'

urlpatterns = [
    path('trainerhomepage/', views.trainerhomepagecall, name='trainerhomepage'),
    path('add_course/', views.add_course, name='add_course'),
    path('course_list/', views.course_list, name='course_list'),
    path('course_detail/<int:pk>/', views.course_detail, name='course_detail'),
    path('enroll_student/<int:course_id>/', views.enroll_student, name='enroll_student'),
    path('enroll_student/', views.enroll_student_default, name='enroll_student_default'),
]
