from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('Dashboard/<staff>',views.dashboard,name="dashboard"),
    # New Creation
    path('new-student/',views.CreateStudent,name="new-student"),
    path('new-staff/',views.Createstaff,name="new-staff"),
    path('new-teacher/',views.Createteacher,name="new-teacher"),
    # Edit Detail
    path('edit-student/<id>',views.EditStudent,name="edit-student"),
    path('edit-staff/<id>',views.Editstaff,name="edit-staff"),
    path('edit-teacher/<id>',views.Editteacher,name="edit-teacher"),
    # Search
    path('search-student/',views.search_student,name='search-student'),
    path('search-staff/',views.search_staff,name='search-staff'),
    path('search-teacher/',views.search_teacher,name='search-teacher'),
    # Profile View
    path('profile/<staff>/<id>',views.ProfileView,name='profile-student'),
]