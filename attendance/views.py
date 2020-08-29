from django.shortcuts import render
from users.models import profile

def Year_Attendance(request,staff,profileid):
    obj = profile.objects.get(id = int(profileid))
    content = {
        'profile_att': obj.attendance.Absent,
        'profile' : obj
    }
    return render(request,'attendance/student_attendance.html',content)

def MarkAttendance(request):
    return render(request,'attendance/markattendance.html')