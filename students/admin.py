from django.contrib import admin
from .models import student
from .forms import studentAdmin

admin.site.register(student, studentAdmin)
