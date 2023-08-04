from django.urls import path,include
from . import views

urlpatterns = [
    path("attendance/<staff>/<profileid>/",views.Year_Attendance,name='yearly-attendance'),
    path("mark-student",views.MarkAttendanceStudent,name='mark-attendance-student'),
    path("mark-teacher",views.MarkAttendanceTeacher,name='mark-attendance-teacher'),
    path("mark-staff",views.MarkAttendanceStaff,name='mark-attendance-staff'),
    path('update-attendance-student/',views.updateAttendanceStudent,name='update-attendance-student'),
    path('update-attendance-teacher/',views.updateAttendanceTeacher,name='update-attendance-teacher'),
    path('update-attendance-staff/',views.updateAttendanceStaff,name='update-attendance-staff'),
    path('fetch-attendance/<int:profileid>',views.fetch_attendance,name='fetch-attendance'),
]