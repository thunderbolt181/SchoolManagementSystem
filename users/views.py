from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib import auth

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Incorrect Username/Password')
    return render(request,'users/login.html')

def logout(request):
    auth.logout(request)
    return redirect('home')