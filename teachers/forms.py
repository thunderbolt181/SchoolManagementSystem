from django import forms
from .models import teachers
from django.contrib.auth.models import User

class TeacherCreateForm(forms.ModelForm):
    class Meta:
        model = teachers
        exclude = ['user','institute','profile_user']