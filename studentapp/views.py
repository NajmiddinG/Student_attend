from django.contrib.auth.forms import PasswordChangeForm
from django.http import HttpResponse
from django.contrib import messages
from django.core.exceptions import ViewDoesNotExist
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from studentapp.models import ContactInfo, Student, StudentAttend, CustomUser
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout, update_session_auth_hash
from django.views.generic import TemplateView

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
    if not request.user.is_authenticated:
        return redirect('login')
    elif request.POST.get('submit') == 'submit':
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
        gender = request.POST.get('gender')

        if roll_no and first_name and last_name and semestr and branch and contact_number and email and city and pincode and address:
            Student.objects.create(roll_no=roll_no, first_name=first_name, last_name=last_name, sem=semestr,
                                   branch=branch, nomer=contact_number, email=email, city=city, pincode=pincode,
                                   address=address, gender=gender)
            messages.success(request, "Muvaffiyatli qo'shildi")
            return redirect('studentmanage')
    elif request.POST.get('back') == 'back':
        return redirect('studentadd')
    context = {
        'title': 'Student add',
        'active': 'student_add'
    }
    return render(request, 'student/add.html', context)


def studentManage(request):
    if not request.user.is_authenticated:
        return redirect('login')
    order = '-id'
    if 'order' in request.POST:
        order = request.POST.get('order')
    if request.GET.get('search'):
        search = request.GET.get('search')
        date = Student.objects.filter(Q(first_name__icontains=search) | Q(email__icontains=search)).order_by(order)
    else:
        date = Student.objects.all().order_by(order)
        date.order_by('last_name')

    page_len = CustomUser.objects.get(id=request.user.id).student_pagination
    if request.GET.get('page_len'):
        page_len = request.GET.get('page_len')
        emp = CustomUser.objects.get(id=request.user.id)
        emp.student_pagination = page_len
        emp.save()
    paginator = Paginator(date, page_len)
    page_number = request.GET.get('pagination')
    page_obj = paginator.get_page(page_number)
    context = {
        'title': 'Manage student',
        'active': 'manage_student',
        'page_len': page_len,
        'page_listing': page_obj,
        'order': order
    }
    return render(request, 'student/manage.html', context)


def editStudent(request, pk):
    if not request.user.is_authenticated:
        return redirect('login')
    edit_data = Student.objects.get(id=pk)
    if request.POST.get('submit') == 'submit':
        edit_data = Student.objects.get(id=pk)
        edit_data.roll_no = request.POST.get('roll_no')
        edit_data.first_name = request.POST.get('first_name')
        edit_data.last_name = request.POST.get('last_name')
        edit_data.sem = request.POST.get('semestr')
        edit_data.branch = request.POST.get('branch')
        edit_data.gender = request.POST.get('gender')
        edit_data.nomer = request.POST.get('contact_number')
        edit_data.email = request.POST.get('email')
        edit_data.city = request.POST.get('city')
        edit_data.pincode = request.POST.get('pincode')
        edit_data.address = request.POST.get('address')
        edit_data.save()
        messages.success(request, 'Muvaffaqqiyati o`zgartirildi')
        return redirect('studentmanage')

    context = {
        'edit_data': edit_data
    }
    return render(request, 'student/add.html', context)


def deleteStudent(request, pk):
    if not request.user.is_authenticated:
        return redirect('login')
    a = Student.objects.get(id=pk)
    a.delete()
    messages.success(request, 'Muvaffaqqiyati o`chirildi')
    return redirect('studentmanage')


def attendanceAdd(request):
    if not request.user.is_authenticated:
        return redirect('login')
    elif request.POST.get('add') == 'submit':
        student = int(request.POST.get('select'))
        date = request.POST.get('date')
        in_time = request.POST.get('in_time')
        out_time = request.POST.get('out_time')
        description = request.POST.get('description')

        if student and date and in_time and out_time and description:
            StudentAttend.objects.create(student=Student.objects.get(id=student), atten_date=date, in_time=in_time,
                                         out_time=out_time, description=description)
            messages.success(request, "Muvaffiyatli qo'shildi")
            return redirect('attendancemanage')
    elif request.POST.get('add') == 'back':
        return redirect('attendanceadd')
    student_name = Student.objects.all().order_by('-id')
    context = {
        'title': 'Attendance add',
        'active': 'attendance_add',
        'student_name': student_name,
    }
    return render(request, 'attendance/add.html', context)


def attendanceManage(request):
    if not request.user.is_authenticated:
        return redirect('login')
    order = '-id'
    if 'order' in request.POST:
        order = request.POST.get('order')
    if request.GET.get('search'):
        search = request.GET.get('search')
        pass
        date = StudentAttend.objects.filter(
            Q(student__first_name__icontains=search) | Q(student__email__icontains=search)).order_by(order)
    else:
        date = StudentAttend.objects.all().order_by(order)
    page_len = CustomUser.objects.get(id=request.user.id).student_pagination
    if request.GET.get('page_len'):
        page_len = request.GET.get('page_len')
        emp = CustomUser.objects.get(id=request.user.id)
        emp.student_pagination = page_len
        emp.save()
    paginator = Paginator(date, page_len)
    page_number = request.GET.get('pagination')
    page_obj = paginator.get_page(page_number)
    context = {
        'title': 'Manage Attendance',
        'active': 'manage_attendance',
        'page_len': page_len,
        'page_listing': page_obj,
        'order': order
    }
    return render(request, 'attendance/manage.html', context)


def editAttendance(request, pk):
    if not request.user.is_authenticated:
        return redirect('login')
    edit_data = StudentAttend.objects.get(id=pk)
    if request.method == 'POST':
        edit_data.student = Student.objects.get(id=int(request.POST.get('select')))
        edit_data.atten_date = request.POST.get('date')
        edit_data.in_time = request.POST.get('in_time')
        edit_data.out_time = request.POST.get('out_time')
        edit_data.description = request.POST.get('description')
        edit_data.save()
        messages.success(request, 'Muvaffaqqiyati o`zgartirildi')
        return redirect('attendancemanage')
    student_name = Student.objects.all().order_by('-id')
    context = {
        'title': 'Attendance edit',
        'active': 'attendance_add',
        'edit_data': edit_data,
        'student_name': student_name,
    }
    return render(request, 'attendance/add.html', context)


def deleteAttendance(request, pk):
    if not request.user.is_authenticated:
        return redirect('login')
    a = StudentAttend.objects.get(id=pk)
    a.delete()
    messages.success(request, 'Muvaffaqqiyati o`chirildi')
    return redirect('attendancemanage')

def changePassword(request):
    if not request.user.is_authenticated:
        return redirect('login')
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, 'Your password was successfully updated!')
            return redirect('dashboard')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    context = {
        'title': 'Change password',
        'form': form
    }
    return render(request, 'dashboard/change_pasword.html', context)


def logout(request):
    auth_logout(request)
    context = {
        'title': 'Logout Attendance',
        'active': 'home'
    }
    return render(request, 'default/home.html', context)