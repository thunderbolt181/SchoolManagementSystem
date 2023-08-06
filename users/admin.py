from django.contrib import admin
from .models import Users
# from .models import profile
from django.contrib.auth.admin import UserAdmin

class CustomUserAdmin(UserAdmin):
    list_display = ('email','username','date_join', 'last_login','is_admin','is_staff',) # details to be displayed in users list
    search_fields = ('email','username',) # Search will search for these fields
    readonly_fields = ('date_join','last_login',) #

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


# admin.site.register(profile)
admin.site.register(Users,CustomUserAdmin)

