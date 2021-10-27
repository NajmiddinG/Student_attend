from django.urls import path
from . import views

urlpatterns = [
    # default template
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.login, name='login'),
    # dashboard
    path('dashboard/', views.dashboard, name='dashboard'),

]
