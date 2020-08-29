from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings
from users import views as user_view
from django.contrib import admin

admin.autodiscover()
admin.site.enable_nav_sidebar = False

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', user_view.login, name='login'),  
    path('logout/', user_view.logout, name='logout'),
    # path('students/',include('students.urls')),
    path('',include('schools.urls')),
    path('',include('attendance.urls')),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
