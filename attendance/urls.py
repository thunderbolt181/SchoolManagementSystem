from django.urls import path,include
from . import views

urlpatterns = [
    path("attendance/<staff>/<profileid>/",views.Year_Attendance,name='yearly-attendance'),
    path("mark/<status>/",views.MarkAttendance,name='mark-attendance'),
    path('update-attendance/',views.update_attendance,name='update-attendance'),
    path('fetch-attendance/<int:profileid>',views.fetch_attendance,name='fetch-attendance'),
]