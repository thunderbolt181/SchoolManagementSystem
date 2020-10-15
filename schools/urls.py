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
    path('edit/<status>/<id>',views.EditStudent,name="edit"),
    # Search
    path('search/<status>/',views.search,name='search'),
    # Profile View
    path('profile/<staff>/<id>/',views.ProfileView,name='profile'),
]