from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('Create',views.create_entry,name="create-entry"),
    path('student-id/<student_id>/',views.studentID,name="student-ID"),
    path('submit_student_fees/<student_id>/',views.submit_student_fees,name="submit_student_fees"),
    path('search-result/',views.search_fun,name='search'),
    path('Edit_Student_Detail/<int:pk>/',views.Edit_Student_Detail.as_view(),name="Edit_Student_Detail")
]