from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
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
    path('password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='dashboard/dashboard.html'), name='password_change_done'),

    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    # student

    path('student/add/', views.studentAdd, name='studentadd'),
    path('student/manage/', views.studentManage, name='studentmanage'),
    # attendance
    path('attendance/add/', views.attendanceAdd, name='attendanceadd'),
    path('attendance/manage/', views.attendanceManage, name='attendancemanage'),
    # edit
    path('edit-student/<int:pk>/', views.editStudent, name='edit_student'),
    path('edit-attendance/<int:pk>/', views.editAttendance, name='edit_attendance'),
    # deletete
    path('delete-student/<int:pk>/', views.deleteStudent, name='delete_student'),
    path('delete-attendance/<int:pk>/', views.deleteAttendance, name='delete_attendance'),
]
