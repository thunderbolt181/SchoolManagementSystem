from django.urls import path,include
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('',views.home,name="student"),
    path('Create',views.create_entry,name="create-entry"),
    path('delete_entry/<student_id>', views.StudentDelete, name='delete-student'),
    path('student-id/<student_id>/',views.studentID,name="student-ID"),
    path('print-id/<student_id>/',views.PrintID,name="print-ID"),
    path('create-backup/',views.CreateBackup,name="create-backup"),
    path('submit_student_fees/<student_id>/',views.submit_student_fees,name="submit_student_fees"),
    path('search-result/',views.search_fun,name='search'),
    path('Edit_Student_Detail/<student_id>/',views.Edit_Student_Detail,name="Edit_Student_Detail")
]