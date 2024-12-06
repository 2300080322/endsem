from django.urls import path
from . import views

app_name = 'employeeapp'

urlpatterns = [
    path('employeehomepage/', views.employeehomepagecall, name='employeehomepage'),
    path('tasks/', views.task_list, name='task_list'),
    path('new_feature/', views.add_new_feature, name='add_new_feature'),
    path('create-profile/', views.create_or_update_profile, name='create_profile'),
    path('view-profile/', views.view_profile, name='view_profile'),
    path('login/', views.login_view, name='login'),
    path('some_error_page/', views.some_error_page, name='some_error_page'),
    # Add this line for error page
    path('track_progress/', views.track_progress, name='track_progress'),
    path('report/', views.report, name='report'),
]
