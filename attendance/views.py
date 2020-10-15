from django.shortcuts import render
from users.models import profile

def Year_Attendance(request,staff,profileid):
    obj = profile.objects.get(id = int(profileid))
    content = {
        'profile_att': obj.attendance.Absent,
        'profile' : obj,
        'extend_tag': f"schools/{staff}_base.html"
    }
    return render(request,'attendance/student_attendance.html',content)
    # if staff == "student":
        # return render(request,'attendance/student_attendance.html',content)
    # elif staff == "teacher":
        # return render(request,'attendance/teacher_attendance.html',content)
    # else:
        # return render(request,'attendance/staff_attendance.html',content)

def MarkAttendance(request):
    return render(request,'attendance/markattendance.html')