from http.client import HTTPResponse

from django.contrib import messages
from django.core.exceptions import ViewDoesNotExist
from django.core.mail import send_mail
from django.shortcuts import render, redirect

from studentapp.models import ContactInfo, Student
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout

def home(request):
    context = {
        'title': 'Home',
        'active': 'home'
    }
    return render(request, 'default/home.html', context)


def about(request):
    context = {
        'title': 'About',
        'active': 'about'
    }
    return render(request, 'default/about.html', context)



def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        number = request.POST['number']
        text = request.POST['text']
        try:
            ContactInfo.objects.create(name=name, email=email, nomer=number, message=text)
            messages.success(request, "Xabaringiz jo'natildi")
            send_mail(str(name) + ' ' + str(number), text, email, ['najmiddinweb@gmail.com'])

        except ViewDoesNotExist:
            return HTTPResponse("Xatolik")

    context = {
        'title': 'Contact',
        'active': 'contact'
    }
    return render(request, 'default/contact.html', context)



def login(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        context = {
            'title': 'Login',
            'active': 'login'
        }
        if request.method == 'POST':
            username = request.POST.get('username_')
            password = request.POST.get('password_')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                messages.success(request, 'Kirish muvaffaqqiyati yakunlandi')
                return redirect('dashboard')
            elif username == "" and password == "":
                messages.error(request, 'Hech narsa kiritmadingiz')
                return render(request, 'default/login.html', context)
            elif username == "":
                messages.error(request, 'Username bo`sh')
                return render(request, 'default/login.html', context)
            elif password == "":
                messages.error(request, 'Password bo`sh')
                return render(request, 'default/login.html', context)
            else:
                messages.error(request, 'Username yoki password xato')
                return render(request, 'default/login.html', context)
        else:
            return render(request, 'default/login.html', context)

def dashboard(request):
    if not request.user.is_authenticated:
        return redirect('login')

    context = {
        'title': 'Dashboard',
        'active': 'dashboard'
    }
    return render(request, 'dashboard/dashboard.html', context)

def studentAdd(request):
    if request.POST.get('submit') == 'submit':
        roll_no = request.POST.get('roll_no')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        semestr = request.POST.get('semestr')
        branch = request.POST.get('branch')
        contact_number = request.POST.get('contact_number')
        email = request.POST.get('email')
        city = request.POST.get('city')
        pincode = request.POST.get('pincode')
        address = request.POST.get('address')
        if roll_no and first_name and last_name and semestr and branch and contact_number and email and city and pincode and address:
            Student.objects.create(roll_no=roll_no, first_name=first_name, last_name=last_name, sem=semestr, branch=branch, nomer=contact_number, email=email, city=city, pincode=pincode, address=address)
            messages.success(request, "Muvaffiyatli qo'shildi")
            return redirect('studentmanage')
    elif request.POST.get('back') == 'back':
        return redirect('dashboard')
    context = {
        'title': 'Student add',
        'active': 'student_add'
    }
    return render(request, 'student/add.html', context)

def studentManage(request):
    context = {
        'title': 'Manage student',
        'active': 'manage_student'
    }
    return render(request, 'student/manage.html', context)


def attendanceAdd(request):
    if request.POST.get('submit') == 'submit':
        roll_no = request.POST.get('roll_no')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        semestr = request.POST.get('semestr')
        branch = request.POST.get('branch')
        contact_number = request.POST.get('contact_number')
        email = request.POST.get('email')
        city = request.POST.get('city')
        pincode = request.POST.get('pincode')
        address = request.POST.get('address')
        if roll_no and first_name and last_name and semestr and branch and contact_number and email and city and pincode and address:
            Student.objects.create(roll_no=roll_no, first_name=first_name, last_name=last_name, sem=semestr, branch=branch, nomer=contact_number, email=email, city=city, pincode=pincode, address=address)
            messages.success(request, "Muvaffiyatli qo'shildi")
            return redirect('studentmanage')
    elif request.POST.get('back') == 'back':
        return redirect('dashboard')
    context = {
        'title': 'Attendance add',
        'active': 'attendance_add'
    }
    return render(request, 'attendance/add.html', context)

def attendanceManage(request):
    context = {
        'title': 'Manage Attendance',
        'active': 'manage_attendance'
    }
    return render(request, 'attendance/manage.html', context)
def logout(request):
    auth_logout(request)
    context = {
        'title': 'Logout Attendance',
        'active': 'home'
    }
    return render(request, 'default/home.html', context)