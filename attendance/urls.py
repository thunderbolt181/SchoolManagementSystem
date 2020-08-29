from django.urls import path,include
from . import views

urlpatterns = [
    path("attendance/<staff>/<profileid>/",views.Year_Attendance,name='yearly-attendance'),
    path("mark/",views.MarkAttendance,name='mark-attendance'),
]