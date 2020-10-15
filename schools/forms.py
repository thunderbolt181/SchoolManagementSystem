from django import forms
from .models import staff
from django.contrib.auth.models import User

class StaffCreateForm(forms.ModelForm):
    class Meta:
        model = staff
        exclude = ['user','profile_user','institute']