from django.shortcuts import render,redirect,reverse
from .models import student
from .forms import StudentCreateForm, submit_fees
from django.contrib import messages
from django.db.models import Q
from django.http import Http404
from django.views.generic import UpdateView
from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.static import serve
import os
import csv

@login_required
def search_fun(request):
    if request.method == "GET":
        if request.GET.get('q') != None and request.GET.get('q') != "":
            search = request.GET['q']
            lookup = Q(Admission_no__icontains = search) | Q(Address__icontains = search) | Q(Name__icontains = search) | Q(Aadhar_Number__icontains = search)
            results = student.objects.filter(lookup).distinct()
            if len(results) != 0:
                page = request.GET.get('page', 1)
                paginator = Paginator(results, 20)
                try:
                    result = paginator.page(page)
                except PageNotAnInteger:
                    result = paginator.page(1)
                except EmptyPage:
                    result = paginator.page(paginator.num_pages)
                content = {
                    'results':result,
                    'result_no':len(results),
                    'search':search,
                }
                return render(request, 'students/search.html',content)
            else:
                content = {
                    'no_result':"No Search Results Found",
                    'search':search,
                }
            return render(request, 'students/search.html',content)
        else:
            return redirect('home')

@login_required
def home(request):
    s = student.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(s, 20)
    try:
        students = paginator.page(page)
    except PageNotAnInteger:
        students = paginator.page(1)
    except EmptyPage:
        students = paginator.page(paginator.num_pages)
    context = {
        'students':students,
        'user':request.user
    }
    return render(request,'students/Main.html',context)

@login_required
def create_entry(request):
    if request.method == 'POST':
        s_form = StudentCreateForm(request.POST,request.FILES)
        if s_form.is_valid():
            S = s_form.save(commit=False)
            S.created_by=request.user
            S.remaning_fees=20000
            S.save()
            return redirect('student-ID',S.id)
    else:
        s_form = StudentCreateForm()
    return render(request, 'students/Create_post.html', {'s_form': s_form,'user':request.user})

@login_required
def studentID(request,student_id):
    user = request.user 
    student_obj = student.objects.get(id=int(student_id))
    s_form = StudentCreateForm(instance=student_obj)
    return render(request,"students/student_id.html",{'student':student_obj,'s_form':s_form,'user':user})

def Edit_Student_Detail(request,student_id):
    student_obj = student.objects.get(id=int(student_id))
    if request.method == 'POST':
        form = StudentCreateForm(request.POST,request.FILES,instance=student_obj)
        if form.is_valid():
            S = form.save(commit=False)
            S.created_by=request.user
            messages.success(request, 'Student Details Updated successfully!')
            S.save()
            return redirect('student-ID',student_obj.id)
    else:
        form = StudentCreateForm(instance=student_obj)
    return render(request, 'students/student_form.html', {'student':student_obj,'form': form,'user':request.user})

@login_required
def submit_student_fees(request,student_id):
    student_obj = student.objects.get(id=int(student_id))
    if request.method == "POST":
        form = submit_fees(request.POST)
        if form.is_valid():
            if form.cleaned_data["Amount_Paying"] <= student_obj.remaning_fees and form.cleaned_data["Amount_Paying"]>0  and form.cleaned_data["Staff_username"] == request.user.username:
                student_obj.remaning_fees = student_obj.remaning_fees-form.cleaned_data["Amount_Paying"]
                student_obj.save()
                messages.success(request, 'Your Fees was Submitted successfully!')
                return redirect('student-ID',student_obj.id)
            else:
                messages.warning(request, 'Please Enter Correct Information')
    else:
        form = submit_fees()
    context={"form":form,'user':request.user,'student':student_obj}
    return render(request,'students/submit-fees.html',context)

@login_required
def StudentDelete(request,student_id): 
    student_object = student.objects.get(id=int(student_id))
    student_object.delete()
    return redirect('home')

@login_required
def PrintID(request,student_id):
    user = request.user
    student_obj = student.objects.get(id=int(student_id))
    s_form = StudentCreateForm(instance=student_obj)
    return render(request,"students/print_id.html",{'student':student_obj,'s_form':s_form,'user':user})

@login_required
def CreateBackup(request):
    fieldnames = list()
    fieldvalue = dict()
    with open('static/downloads/students.csv','w') as csv_file:
        form = StudentCreateForm()
        for j in form:
            fieldnames.append(j.name)
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames,lineterminator = '\n')
        writer.writeheader()
        for i in student.objects.all():
            for j in fieldnames:
                try:
                    fieldvalue[f'{j}']=(getattr(i, f'{j}'))
                except:
                    fieldvalue[f'{j}']=(getattr(i.eav, f'{j}'))
            writer.writerow(fieldvalue)
    filepath = 'static/downloads/students.csv'
    return serve(request, os.path.basename(filepath),os.path.dirname(filepath))