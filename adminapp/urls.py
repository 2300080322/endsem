# adminapp/urls.py
from django.urls import path
from . import views
app_name = 'adminapp'
urlpatterns = [
    path('', views.homepagecall, name='projecthomepage'),
    path('login/', views.loginpagecall, name='LoginPage'),
    path('register', views.registerpagecall, name='registerpagecall'),
    path('UserRegisterLogic/', views.UserRegisterLogic, name='UserRegisterLogic'),
    path('Register/', views.registerpagecall, name='Register'),
    path('UserLoginLogic/', views.UserLoginLogic, name='UserLoginLogic'),
    path('logout/', views.logout, name='logout'),
    path('submit_feedback/', views.submit_feedback, name='submit_feedback'),
    path('feedback_list/', views.feedback_list, name='feedback_list'),
    path('feedback_success/', views.feedback_success, name='feedback_success'),
    path('dashboard/', views.admin_dashboard, name='dashboard'),
    path('Register', views.registerpagecall, name='Register'),
]
