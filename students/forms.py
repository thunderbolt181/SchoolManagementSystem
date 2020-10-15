from django import forms
from .models import student
from django.contrib.auth.models import User

class StudentCreateForm(forms.ModelForm):
    class Meta:
        model = student
        exclude = ['user',"institute",'profile_user']
        widgets = {
            'Note_about_Student': forms.TextInput(attrs={'type': 'textarea'}),
        }