from django.urls import path
from . import views

urlpatterns = [
    path('',views.homeStudent,name="home-student"),
    path('student-profile',views.StudentView,name='student-profile'),
]