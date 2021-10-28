from django.urls import path
from . import views

urlpatterns = [
    # default template
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.login, name='login'),
    # logout
    path('logout/', views.logout, name='logout'),
    # dashboard
    path('dashboard/', views.dashboard, name='dashboard'),
    # student
    path('student/add/', views.studentAdd, name='studentadd'),
    path('student/manage/', views.studentManage, name='studentmanage'),
    # attendance
    path('attendance/add/', views.attendanceAdd, name='attendanceadd'),
    path('attendance/manage/', views.attendanceManage, name='attendancemanage')
]
