from django.shortcuts import render
from django.shortcuts import render,redirect,reverse
from django.contrib import messages
from django.db.models import Q
from django.http import Http404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import os
import csv
from django.contrib import auth

def home(request):
    return render(request,'schools/home.html')
