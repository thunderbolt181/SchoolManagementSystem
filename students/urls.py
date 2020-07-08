from django.urls import path,include
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('',views.home,name="home"),
    path('Create',views.create_entry,name="create-entry"),
    path('delete_entry/<student_id>', views.StudentDelete, name='delete-student'),
    path('student-id/<student_id>/',views.studentID,name="student-ID"),
    path('submit_student_fees/<student_id>/',views.submit_student_fees,name="submit_student_fees"),
    path('search-result/',views.search_fun,name='search'),
    path('Edit_Student_Detail/<student_id>/',views.Edit_Student_Detail,name="Edit_Student_Detail")
]