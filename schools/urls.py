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
    path('edit/<status>/<id>',views.EditDetails,name="edit"),
    # Search
    path('search/<status>/',views.search,name='search'),
    # Users profile View
    path('users/<staff>/<id>/',views.UsersView,name='users'),
]