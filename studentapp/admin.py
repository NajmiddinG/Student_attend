from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.db.models import fields
from django.utils.translation import gettext_lazy as _
from .models import CustomUser, Student, StudentAttend, ContactInfo

@admin.register(CustomUser)
class UserAdmin(UserAdmin):
    list_display = ('id', 'username', 'email', 'first_name', 'last_name', 'is_staff')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    search_fields = ('username', 'first_name', 'last_name', 'email')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
        (_('CustomFields'), {'fields': ('image',)}),
    )

@admin.register(Student)
class Student(admin.ModelAdmin):
    list_display = ('roll_no', 'first_name', 'last_name', 'sem', 'branch', 'gender', 'nomer', 'email', 'city', 'pincode', 'address')
    list_filter = ('roll_no', 'first_name', 'last_name', 'sem', 'branch', 'gender', 'nomer', 'email', 'city', 'pincode', 'address')


@admin.register(StudentAttend)
class StudentAttend(admin.ModelAdmin):
    list_display = ('student', 'atten_date', 'in_time', 'out_time', 'description')
    list_filter = ('student', 'atten_date', 'in_time', 'out_time', 'description')

@admin.register(ContactInfo)
class ContactInfo(admin.ModelAdmin):
    list_display = ('name', 'email', 'nomer', 'message')
    list_filter = ('name', 'email', 'nomer', 'message')

