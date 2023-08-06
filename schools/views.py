from django.shortcuts import render,redirect,reverse
from django.contrib import messages
from django.db.models import Q
from django.http import Http404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from students.models import student
from teachers.models import teachers
from students.forms import StudentCreateForm
from .forms import StaffCreateForm
# from users.models import profile
from users.forms import UserRegistraionForm, UserEditForm
from .models import institutes,staff
from teachers.forms import TeacherCreateForm
from attendance.models import attendance
import os
import json
from django.db import connection

def staff_test(user):
    if user.status=='staff':
        return True

def dbms_cursor(query):
    with connection.cursor() as cursor:
        cursor.execute(query)
        result = cursor.fetchall()
    return result

@login_required
@user_passes_test(staff_test)
def home(request):
    id = request.user.staff.institute.id
    count = dbms_cursor(f'''SELECT COUNT(id) FROM students_student WHERE institute_id = {id}
                           UNION ALL 
                           SELECT COUNT(id) FROM schools_staff WHERE institute_id =  {id}
                           UNION ALL 
                           SELECT COUNT(id) FROM teachers_teachers WHERE institute_id = {id}
                        ''')
    context={
        'user':request.user,
        'count':count,
    }
    return render(request,'schools/home.html',context)

@login_required
@user_passes_test(staff_test)
def UsersView(request,staff,id):
    if staff == 'student':
        context = {
            'profile' : request.user.staff.institute.student_set.get(id = int(id)),
        }
        return render(request,'schools/student_Profile.html',context)
    elif staff == 'teacher':
        context = {
            'profile' : request.user.staff.institute.teachers_set.get(id = int(id)),
        }
        return render(request,'schools/teacher_Profile.html',context)
    else :
        context = {
            'profile' : request.user.staff.institute.staff_set.get(id = int(id)),
        }
        return render(request,'schools/staff_Profile.html',context)

@login_required
@user_passes_test(staff_test)
def dashboard(request,staff):
    if staff == 'student' :
        results = request.user.staff.institute.student_set.all()
    elif staff == 'staff' :
        results = request.user.staff.institute.staff_set.all()
    else:
        results = request.user.staff.institute.teachers_set.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(results, 20)
    try:
        result = paginator.page(page)
    except PageNotAnInteger:
        result = paginator.page(1)
    except EmptyPage:
        result = paginator.page(paginator.num_pages)
    content = {
        'profiles':result,
    }
    if staff == 'student':
        return render(request,'schools/student_dashboard.html',content)
    elif staff == 'staff' :
        return render(request,'schools/staff_dashboard.html',content)
    else:
        return render(request,'schools/teacher_dashboard.html',content)

# ******************************************** Search Views **********************************************************

@login_required
@user_passes_test(staff_test)
def search(request,status):
    if request.method == "GET":
        if request.GET.get('q') != None and request.GET.get('q') != "":
            search = request.GET['q']
            if status == 'student':
                lookup = Q(Admission_no__icontains = search) | Q(user__first_name__icontains = search) | Q(user__last_name__icontains = search)
                results = request.user.staff.institute.student_set.filter(lookup)
            elif status == 'staff':
                lookup = Q(Staff_ID__icontains = search) | Q(user__first_name__icontains = search) | Q(user__last_name__icontains = search)
                results = request.user.staff.institute.staff_set.filter(lookup)
            else:
                lookup = Q(Faculty_ID__icontains = search) | Q(user__first_name__icontains = search) | Q(user__last_name__icontains = search)
                results = request.user.staff.institute.teachers_set.filter(lookup)
            if len(results) !=0:
                content = {
                    'profiles':results,
                    'result_no':len(results),
                    'search':search,
                    'extend_tag': f"schools/{status}_base.html",
                    'status': status,
                }
                return render(request, 'schools/search_result.html',content)
            else:
                content = {
                    'no_result':"No Search Results Found",
                    'result_no':" 0",
                    'search':search,
                    'extend_tag': f"schools/{status}_base.html"
                }
                return render(request, 'schools/search_result.html',content)
        else:
            if status == 'student':
                return redirect("dashboard", "student")
            elif status == 'staff':
                return redirect("dashboard", "staff")
            else:
                return redirect("dashboard", "teacher")

# **************************************** Creating Forms ***********************************************

@login_required
@user_passes_test(staff_test)
def CreateStudent(request):
    if request.method=='POST':
        user_form = UserRegistraionForm(request.POST,request.FILES)
        student_form = StudentCreateForm(request.POST)
        if user_form.is_valid() and student_form.is_valid():
            U = user_form.save(commit=False)
            S = student_form.save(commit=False)
            U.status = "student"
            S.institute = request.user.staff.institute
            S.user= U
            U.save()
            S.save()
            return redirect('dashboard','student')
    else:
        user_form = UserRegistraionForm()
        student_form = StudentCreateForm()
    context={
        'user_form' : user_form,
        'staff_form' : student_form,
    }
    return render(request,'schools/student_new_entry.html',context)

@login_required
@user_passes_test(staff_test)
def Createstaff(request):
    if request.method=='POST':
        user_form = UserRegistraionForm(request.POST,request.FILES)
        staff_form = StaffCreateForm(request.POST)
        if user_form.is_valid() and staff_form.is_valid():
            U = user_form.save(commit=False)
            S = staff_form.save(commit=False)
            U.status = "staff"
            S.institute = request.user.staff.institute
            S.user=U
            U.save()
            S.save()
            return redirect('dashboard','staff')
    else:
        user_form = UserRegistraionForm()
        staff_form = StaffCreateForm()
    context={
        'user_form' : user_form,
        'staff_form' : staff_form,
    }
    return render(request,'schools/staff_new_entry.html',context)

@login_required
@user_passes_test(staff_test)
def Createteacher(request):
    if request.method=='POST':
        user_form = UserRegistraionForm(request.POST,request.FILES)
        teacher_form = TeacherCreateForm(request.POST)
        if user_form.is_valid() and teacher_form.is_valid():
            U = user_form.save(commit=False)
            T = teacher_form.save(commit=False)
            U.status = "teacher"
            T.user=U
            T.institute = request.user.staff.institute
            U.save()
            T.save()
            return redirect('dashboard','teacher')
    else:
        user_form = UserRegistraionForm()
        teacher_form = TeacherCreateForm()
    context={
        'user_form' : user_form,
        'staff_form' : teacher_form,
    }
    return render(request,'schools/teacher_new_entry.html',context)

# **************************************** Editing Forms ***********************************************

@login_required
@user_passes_test(staff_test)
def EditDetails(request,status,id):
    if status == 'student':
        obj = student.objects.get(id=int(id))
    elif status == 'staff':
        obj = staff.objects.get(id=int(id))
    else:
        obj = teachers.objects.get(id=int(id))
    if request.method=='POST':
        if status == 'student':
            status_form = StudentCreateForm(request.POST,instance=obj)
        elif status == 'staff':
            status_form = StaffCreateForm(request.POST,instance=obj)
        else:
            status_form = TeacherCreateForm(request.POST,instance=obj)
        user_form = UserEditForm(request.POST,request.FILES,instance=obj.user)
        if user_form.is_valid() and status_form.is_valid():
            user_form.save()
            status_form.save()
            return redirect("users",status,id)
    else:
        user_form = UserEditForm(instance=obj.user)
        if status == 'student':
            status_form = StudentCreateForm(instance=obj)
        elif status == 'staff':
            status_form = StaffCreateForm(instance=obj)
        else:
            status_form = TeacherCreateForm(instance=obj)
    context={
        'user_form' : user_form,
        'staff_form' : status_form,
        'extend_tag': f"schools/{status}_base.html"
    }
    return render(request,'schools/edit_entry.html',context)