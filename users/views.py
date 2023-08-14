from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib import auth
from django.http import Http404

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            try:
                if user.status == 'staff':
                    auth.login(request, user)
                    return redirect('home-staff')
                elif user.status == 'student':
                    auth.login(request,user)
                    return redirect('home-student')
                else:
                    messages.error(request, 'User has no permission to access this link')
            except Exception as e:
                messages.error(request, "User Profile does not exits.")
        else:
            messages.error(request, 'Incorrect Username/Password')
    return render(request,'users/login.html')

def logout(request):
    auth.logout(request)
    return redirect('login')