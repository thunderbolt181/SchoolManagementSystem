from django.shortcuts import  render,redirect,reverse
from users.models import profile
from django.contrib.auth.decorators import login_required, user_passes_test
from django.db.models import Q
from django.http import JsonResponse
from attendance.models import attendance
import json
import django.dispatch

@login_required
def Year_Attendance(request,staff,profileid):
    obj = profile.objects.get(id = int(profileid))
    content = {
        'profile_att': obj.attendance.Absent,
        'profile' : obj,
        'extend_tag': f"schools/{staff}_base.html"
    }
    return render(request,'attendance/view_attendance.html',content)

@login_required
def fetch_attendance(request,profileid):
    if request.is_ajax and request.method == 'GET':
        try:
            results = attendance.objects.get(id=(profileid))
            return JsonResponse({'0':"True",'1':results.Absent})
        except:
            return JsonResponse({'0':'False'})
    else:
        return JsonResponse({'0':'False'})

@login_required
def update_attendance(request):
    if request.is_ajax and request.method == 'POST':
        data = json.loads(request.POST['attendance'])
        month = str(int(data['month'])-1)
        date = str(int(data['date']))
        att=[]
        lookup = Q(Class__icontains = data['c']) & Q(Section__icontains = data['s'])
        results = request.user.staff.institute.student_set.filter(lookup).order_by('Roll_no')
        try:
            for i in results:
                if str(i.Roll_no) in data.keys():
                    i.profile_user.attendance.Absent[month][date][0] = data[f'{i.Roll_no}']
                    att.append(i.profile_user.attendance)
            attendance.objects.bulk_update(att,['Absent'])
            return JsonResponse({'is_taken':'True'})
        except:
            return JsonResponse({'is_taken':'False'})
    else:
        return JsonResponse({'is_taken':'False'})

@login_required
def MarkAttendance(request,status):
    if request.method == 'GET':
        if request.GET.get('class') != None and request.GET.get('section') != None and request.GET.get('class') != "" and request.GET.get('section') != "":
            c = request.GET['class']
            s = request.GET['section']
            if status == 'student':
                lookup = Q(Class__icontains = c) & Q(Section__icontains = s)
                results = request.user.staff.institute.student_set.filter(lookup).order_by('Roll_no')
            elif status == 'staff':
                pass
            else:
                pass
            if len(results) !=0:
                content = {
                    'profiles':results,
                    'result_no':len(results),
                    'class':c,
                    'section':s,
                    'extend_tag': f"schools/{status}_base.html",
                    'status': status,
                }
                return render(request, 'attendance/markattandance.html',content)
            else:
                content = {
                    'no_result':"No Search Results Found",
                    'result_no':" 0",
                    'class':c,
                    'section':s,
                    'extend_tag': f"schools/{status}_base.html"
                }
                return render(request, 'attendance/markattandance.html',content)
        else:
            if status == 'student':
                return redirect("dashboard", "student")
            elif status == 'staff':
                return redirect("dashboard", "staff")
            else:
                return redirect("dashboard", "teacher")