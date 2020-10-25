from .models import profile
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm 

class UserRegistraionForm(UserCreationForm):
    email=forms.EmailField()
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)

    class Meta:
        model = User
        fields = ['username', 'email','first_name','last_name' ,'password1', 'password2']

class UserEditForm(forms.ModelForm):
    email=forms.EmailField()
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)

    class Meta:
        model = User
        fields = ['username', 'email','first_name','last_name']

class ProfileCreateForm(forms.ModelForm):
    class Meta:
        model = profile
        exclude = ['user','status']
        widgets = {
            'DOB': forms.TextInput(attrs={'type':'date'}),
        }