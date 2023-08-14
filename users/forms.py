from .models import Users
from django import forms
from django.contrib.auth.forms import UserCreationForm 

class UserRegistraionForm(UserCreationForm):
    email=forms.EmailField()
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)

    class Meta:
        model = Users
        fields = ['username', 'email','password1', 'password2','first_name','last_name','DOB',
                  'Gender','phone_1','phone_2','Aadhar_Number','Fathers_Name','Fathers_Occupation',
                  "Mothers_Name",'Mothers_Occupation','House_No','Street_Name','city','PIN_Code','Category',
                  'Profile_pic'] # user to format the ordering of the fields in ui.

        # exclude = ['password','is_admin','is_active','is_superuser','is_staff','date_join','last_login',"status"]

class UserEditForm(forms.ModelForm):
    email=forms.EmailField()
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)

    class Meta:
        model = Users
        exclude = ['groups','user_permissions','password','is_admin','is_active','is_superuser','is_staff','date_join','last_login',"status"]