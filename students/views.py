from django.shortcuts import render,redirect,reverse
from django.contrib import messages
from django.db.models import Q
from django.http import Http404
from django.views.generic import UpdateView
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.static import serve
import os
import csv

def student_test(user):
    if user.status=='student': return True

def homeStudent(request):
    context = {
        'user': request.user,
    }
    return render(request,'students/home.html',context)

def StudentView(request):
    context = {
        'user' : request.user,
    }
    return render(request,'students/student_Profile.html',context)
