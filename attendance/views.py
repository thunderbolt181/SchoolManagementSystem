from django.shortcuts import  render,redirect,reverse
from users.models import Users
from django.contrib.auth.decorators import login_required, user_passes_test
from django.db.models import Q
from django.http import JsonResponse
from attendance.models import attendance
import json
import django.dispatch

@login_required
def Year_Attendance(request,staff,profileid):
    if request.user.status == 'staff':
        obj = Users.objects.get(id = int(profileid))
        content = {
            'profile_att': obj.attendance.Absent,
            'profile' : obj,
            'extend_tag': f"schools/{staff}_base.html"
        }
    elif request.user.status == 'student':
        content = {
            'profile_att': request.user.attendance.Absent,
            'profile' : request.user,
            'extend_tag': f"students/{staff}_base.html"
        }
    return render(request,'attendance/view_attendance.html',content)

@login_required
def fetch_attendance(request,profileid):
    if request.method == 'GET':
        try:
            results = attendance.objects.get(id=(profileid))
            return JsonResponse({'0':"True",'1':results.Absent})
        except:
            return JsonResponse({'0':'False'})
    else:
        return JsonResponse({'0':'False'})

@login_required
def updateAttendanceStudent(request):
    if request.method == 'POST':
        data = json.loads(request.POST['attendance'])
        month = str(int(data['month'])-1)
        date = str(int(data['date']))
        att=[]
        lookup = Q(Class__icontains = int(data['c'])) & Q(Section__icontains = data['s'])
        results = request.user.staff.institute.student_set.filter(lookup).order_by('Roll_no')
        try:
            for i in results:
                if str(i.Roll_no) in data.keys():
                    i.user.attendance.Absent[month][date][0] = data[f'{i.Roll_no}']
                    att.append(i.user.attendance)
            attendance.objects.bulk_update(att,['Absent'])
            return JsonResponse({'is_taken':'True'})
        except:
            return JsonResponse({'is_taken':'False'})
    else:
        return JsonResponse({'is_taken':'False'})

@login_required
def updateAttendanceTeacher(request):
    if request.method == 'POST':
        print('teacher attendance')
        data = json.loads(request.POST['attendance'])
        month = str(int(data['month'])-1)
        date = str(int(data['date']))
        att=[]
        lookup = Q(Faculty_ID__icontains = data['search']) | Q(user__first_name__icontains = data['search']) | Q(user__last_name__icontains = data['search'])
        results = request.user.staff.institute.teachers_set.filter(lookup)
        try:
            for i in results:
                if str(i.Faculty_ID) in data.keys():
                    i.user.attendance.Absent[month][date][0] = data[f'{i.Faculty_ID}']
                    att.append(i.user.attendance)
            attendance.objects.bulk_update(att,['Absent'])
            return JsonResponse({'is_taken':'True'})
        except:
            return JsonResponse({'is_taken':'False'})
    else:
        return JsonResponse({'is_taken':'False'})

@login_required
def updateAttendanceStaff(request):
    if request.method == 'POST':
        data = json.loads(request.POST['attendance'])
        month = str(int(data['month'])-1)
        date = str(int(data['date']))
        att=[]
        lookup = Q(Staff_ID__icontains = data['search']) | Q(user__first_name__icontains = data['search']) | Q(user__last_name__icontains = data['search'])
        results = request.user.staff.institute.staff_set.filter(lookup)
        try:
            for i in results:
                if str(i.Staff_ID) in data.keys():
                    i.user.attendance.Absent[month][date][0] = data[f'{i.Staff_ID}']
                    att.append(i.user.attendance)
            attendance.objects.bulk_update(att,['Absent'])
            return JsonResponse({'is_taken':'True'})
        except:
            return JsonResponse({'is_taken':'False'})
    else:
        return JsonResponse({'is_taken':'False'})

@login_required
def MarkAttendanceStudent(request):
    if request.method == 'GET':
        if request.GET.get('class') != None and request.GET.get('section') != None and request.GET.get('class') != "" and request.GET.get('section') != "":
            c = request.GET['class']
            s = request.GET['section']
            lookup = Q(Class__icontains = c) & Q(Section__icontains = s)
            results = request.user.staff.institute.student_set.filter(lookup).order_by('Roll_no')
            if len(results) !=0:
                content = {
                    'profiles':results,
                    'result_no':len(results),
                    'class':c,
                    'section':s,
                    'extend_tag': f"schools/student_base.html",
                    'status':"student",
                }
                return render(request, 'attendance/markattandance.html',content)
            else:
                content = {
                    'no_result':"No Search Results Found",
                    'result_no':" 0",
                    'class':c,
                    'section':s,
                    'extend_tag': f"schools/student_base.html"
                }
                return render(request, 'attendance/markattandance.html',content)
        else:
            return redirect("dashboard", "student")

@login_required
def MarkAttendanceTeacher(request):
    if request.method == 'GET':
        if request.GET.get('search') != None and request.GET.get('search') != "":
            search = request.GET['search']
            lookup = Q(Faculty_ID__icontains = search) | Q(user__first_name__icontains = search) | Q(user__last_name__icontains = search)
            results = request.user.staff.institute.teachers_set.filter(lookup)
            if len(results) !=0:
                content = {
                    'profiles':results,
                    'result_no':len(results),
                    'search':search,
                    'extend_tag': f"schools/teacher_base.html",
                    'status':"teacher",
                }
                return render(request, 'attendance/markattandance.html',content)
            else:
                content = {
                    'no_result':"No Search Results Found",
                    'result_no':" 0",
                    'search':search,
                    'extend_tag': f"schools/teacher_base.html"
                }
                return render(request, 'attendance/markattandance.html',content)
        else:
            return redirect("dashboard", "teacher")
        
@login_required
def MarkAttendanceStaff(request):
    if request.method == 'GET':
        if request.GET.get('search') != None and request.GET.get('search') != "":
            search = request.GET['search']
            lookup = Q(Staff_ID__icontains = search) | Q(user__first_name__icontains = search) | Q(user__last_name__icontains = search)
            results = request.user.staff.institute.staff_set.filter(lookup)
            if len(results) !=0:
                content = {
                    'profiles':results,
                    'result_no':len(results),
                    'search':search,
                    'extend_tag': f"schools/staff_base.html",
                    'status':"staff",
                }
                return render(request, 'attendance/markattandance.html',content)
            else:
                content = {
                    'no_result':"No Search Results Found",
                    'result_no':" 0",
                    'search':search,
                    'extend_tag': f"schools/staff_base.html"
                }
                return render(request, 'attendance/markattandance.html',content)
        else:
            return redirect("dashboard", "staff")