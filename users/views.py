from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib import auth

def logout(request):
    auth.logout(request)
    return redirect('home')