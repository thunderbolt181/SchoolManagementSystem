from django.shortcuts import render,redirect,reverse
from django.contrib import messages
from django.db.models import Q
from django.http import Http404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from students.models import student
from teachers.models import teachers
from students.forms import StudentCreateForm
from .forms import StaffCreateForm
from users.models import profile
from users.forms import ProfileCreateForm, UserRegistraionForm, UserEditForm
from .models import institutes
from teachers.forms import TeacherCreateForm
from attendance.models import attendance
import os

@login_required
def ProfileView(request,staff,id):
    obj = request.user.profile.institute.profile_set.get(id = int(id))
    if staff == 'student':
        context = {
            'profile' : obj,
        }
        return render(request,'schools/student_Profile.html',context)
    elif staff == 'teacher':
        context = {
            'profile' : obj,
        }
        return render(request,'schools/teacher_Profile.html',context)
    else :
        context = {
            'profile' : obj,
        }
        return render(request,'schools/staff_Profile.html',context)

@login_required
def home(request):
    context={
        'user':request.user
    }
    return render(request,'schools/home.html',context)
    
@login_required
def dashboard(request,staff):
    if staff == 'student' :
        lookup = Q(status__icontains = 'student')
    elif staff == 'staff' :
        lookup = Q(status__icontains = 'staff')
    else:
        lookup = Q(status__icontains = 'teacher')
    results = request.user.profile.institute.profile_set.filter(lookup)
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

# ******************************************** Search Views **********************************************************8888

def search_teacher(request):
    if request.method == "GET":
        if request.GET.get('q') != None and request.GET.get('q') != "":
            search = request.GET['q'].strip()
            lookup = Q(user__teachers__Faculty_ID__icontains = search) | (Q(user__first_name__icontains = search) & Q(status__icontains = "teacher") )
            results = request.user.profile.institute.profile_set.filter(lookup)
            if len(results) !=0:
                content = {
                    'profiles':results,
                    'result_no':len(results),
                    'search':search,
                }
                return render(request, 'schools/teacher_search.html',content)
            else:
                content = {
                    'no_result':"No Search Results Found",
                    'result_no':" 0",
                    'search':search,
                }
                return render(request, 'schools/teacher_search.html',content)
        else:
            return redirect("dashboard", "teacher")

def search_staff(request):
    if request.method == "GET":
        if request.GET.get('q') != None and request.GET.get('q') != "":
            search = request.GET['q'].strip()
            lookup = Q(user__staff__Staff_ID__icontains = search) | (Q(user__first_name__icontains = search) & Q(status__icontains = "staff") )
            results = request.user.profile.institute.profile_set.filter(lookup)
            if len(results) !=0:
                content = {
                    'profiles':results,
                    'result_no':len(results),
                    'search':search,
                }
                return render(request, 'schools/staff_search.html',content)
            else:
                content = {
                    'no_result':"No Search Results Found",
                    'result_no':" 0",
                    'search':search,
                }
                return render(request, 'schools/staff_search.html',content)
        else:
            return redirect("dashboard", "staff")

def search_student(request):
    if request.method == "GET":
        if request.GET.get('q') != None and request.GET.get('q') != "":
            search = request.GET['q'].strip()
            lookup = Q(user__student__Admission_no__icontains = search) | (Q(user__first_name__icontains = search) & Q(status__icontains = "student") )
            results = request.user.profile.institute.profile_set.filter(lookup)
            if len(results) !=0:
                content = {
                    'profiles':results,
                    'result_no':len(results),
                    'search':search,
                }
                return render(request, 'schools/student_search.html',content)
            else:
                content = {
                    'no_result':"No Search Results Found",
                    'result_no':" 0",
                    'search':search,
                }
                return render(request, 'schools/student_search.html',content)
        else:
            return redirect("dashboard", "student")

# **************************************** Creating Forms ***********************************************

def CreateStudent(request):
    if request.method=='POST':
        user_form = UserRegistraionForm(request.POST)
        profile_form = ProfileCreateForm(request.POST,request.FILES)
        student_form = StudentCreateForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid() and student_form.is_valid():
            U = user_form.save()
            P = profile_form.save(commit=False)
            S = student_form.save(commit=False)
            S.user= U
            P.user= U
            P.status = "student"
            P.institute = request.user.profile.institute
            P.save()
            S.save()
            attendance.objects.create(user_profile=P,absent="{}")
            return redirect('dashboard','student')
    else:
        user_form = UserRegistraionForm()
        profile_form = ProfileCreateForm()
        student_form = StudentCreateForm()
    context={
        'user_form' : user_form,
        'profile_form' : profile_form,
        'staff_form' : student_form,
    }
    return render(request,'schools/student_new_entry.html',context)

def Createstaff(request):
    if request.method=='POST':
        user_form = UserRegistraionForm(request.POST)
        profile_form = ProfileCreateForm(request.POST,request.FILES)
        staff_form = StaffCreateForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid() and staff_form.is_valid():
            U = user_form.save()
            P = profile_form.save(commit=False)
            S = staff_form.save(commit=False)
            S.user=U
            P.user=U
            P.status = "staff"
            P.institute = request.user.profile.institute
            P.save()
            S.save()
            attendance.objects.create(user_profile=P,absent="{}")
            return redirect('dashboard','staff')
    else:
        user_form = UserRegistraionForm()
        profile_form = ProfileCreateForm()
        staff_form = StaffCreateForm()
    context={
        'user_form' : user_form,
        'profile_form' : profile_form,
        'staff_form' : staff_form,
    }
    return render(request,'schools/staff_new_entry.html',context)

def Createteacher(request):
    if request.method=='POST':
        user_form = UserRegistraionForm(request.POST)
        profile_form = ProfileCreateForm(request.POST,request.FILES)
        teacher_form = TeacherCreateForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid() and teacher_form.is_valid():
            U = user_form.save()
            P = profile_form.save(commit=False)
            T = teacher_form.save(commit=False)
            T.user=U
            P.user=U
            P.status = "teacher"
            P.institute = request.user.profile.institute
            P.save()
            T.save()
            attendance.objects.create(user_profile=P,absent="{}")
            return redirect('dashboard','teacher')
    else:
        user_form = UserRegistraionForm()
        profile_form = ProfileCreateForm()
        teacher_form = TeacherCreateForm()
    context={
        'user_form' : user_form,
        'profile_form' : profile_form,
        'staff_form' : teacher_form,
    }
    return render(request,'schools/teacher_new_entry.html',context)

# **************************************** Editing Forms ***********************************************

def EditStudent(request,id):
    obj = profile.objects.get(id=int(id))
    if request.method=='POST':
        user_form = UserEditForm(request.POST,instance=obj.user)
        profile_form = ProfileCreateForm(request.POST,request.FILES,instance=obj)
        student_form = StudentCreateForm(request.POST,instance=obj.user.student)
        if user_form.is_valid() and profile_form.is_valid() and student_form.is_valid():
            user_form.save()
            profile_form.save()
            student_form.save()
            return redirect('dashboard','student')
    else:
        user_form = UserEditForm(instance=obj.user)
        profile_form = ProfileCreateForm(instance=obj)
        student_form = StudentCreateForm(instance=obj.user.student)
    context={
        'user_form' : user_form,
        'profile_form' : profile_form,
        'staff_form' : student_form,
    }
    return render(request,'schools/student_edit_entry.html',context)

def Editstaff(request,id):
    obj = profile.objects.get(id=int(id))
    if request.method=='POST':
        user_form = UserEditForm(request.POST,instance=obj.user)
        profile_form = ProfileCreateForm(request.POST,request.FILES,instance=obj)
        staff_form = StaffCreateForm(request.POST,instance=obj.user.staff)
        if user_form.is_valid() and profile_form.is_valid() and staff_form.is_valid():
            user_form.save()
            profile_form.save()
            staff_form.save()
            return redirect('dashboard','staff')
    else:
        user_form = UserEditForm(instance=obj.user)
        profile_form = ProfileCreateForm(instance=obj)
        staff_form = StaffCreateForm(instance=obj.user.staff)
    context={
        'user_form' : user_form,
        'profile_form' : profile_form,
        'staff_form' : staff_form,
    }
    return render(request,'schools/staff_edit_entry.html',context)

def Editteacher(request,id):
    obj = profile.objects.get(id=int(id))
    if request.method=='POST':
        user_form = UserEditForm(request.POST,instance=obj.user)
        profile_form = ProfileCreateForm(request.POST,request.FILES,instance=obj)
        teacher_form = TeacherCreateForm(request.POST,instance=obj.user.teachers)
        if user_form.is_valid() and profile_form.is_valid() and teacher_form.is_valid():
            user_form.save()
            profile_form.save()
            teacher_form.save()
            return redirect('dashboard','teacher')
    else:
        user_form = UserEditForm(instance=obj.user)
        profile_form = ProfileCreateForm(instance=obj)
        teacher_form = TeacherCreateForm(instance=obj.user.teachers)
    context={
        'user_form' : user_form,
        'profile_form' : profile_form,
        'staff_form' : teacher_form,
    }
    return render(request,'schools/teacher_edit_entry.html',context)