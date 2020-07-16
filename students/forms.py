from django import forms
from students.models import student
from django.contrib.auth.models import User
from eav.forms import BaseDynamicEntityForm
from eav.admin import BaseEntityAdmin

class StudentCreateForm(forms.ModelForm):

    class Meta:
        model = student
        fields = ['Admission_no','Name','DOB','Gender','Phone','Phone_Other','Email',
            'Class','Aadhar_Number','Fathers_Name','Fathers_Occupation','Mothers_Name','Mothers_Occupation',
            'Relegion','caste','Category','Address','Nationality','Profile_pic','Aadhar_Card',"Marksheet_10th",
            "Marksheet_12th","Caste_Certificate",'Note_about_Student']

class studentAdminForm(BaseDynamicEntityForm):
    class Meta:
        model = student
        fields = ['Admission_no','Name','DOB','Gender','Phone','Phone_Other','Email',
            'Class','Aadhar_Number','Fathers_Name','Fathers_Occupation','Mothers_Name','Mothers_Occupation',
            'Relegion','caste','Category','Address','Nationality','Profile_pic','Aadhar_Card',"Marksheet_10th",
            "Marksheet_12th","Caste_Certificate",'Note_about_Student']
        widgets = {
            'DOB': forms.TextInput(attrs={'type': 'date'}),
        }

class studenteditAdminForm(BaseDynamicEntityForm):
    class Meta:
        model = student
        fields = ['Name','DOB','Gender','Phone','Phone_Other','Email','Class','Aadhar_Number',
            'Fathers_Name','Fathers_Occupation','Mothers_Name','Mothers_Occupation','Relegion',
            'caste','Category','Address','Nationality','Profile_pic','Aadhar_Card',"Marksheet_10th",
            "Marksheet_12th","Caste_Certificate",'Note_about_Student']
        widgets = {
            'DOB': forms.TextInput(attrs={'type': 'date'}),
        }

class studentAdmin(BaseEntityAdmin):
    form = studentAdminForm

class submit_fees(forms.Form):
    Amount_Paying = forms.IntegerField()
    Staff_username = forms.CharField(max_length=100)

    class Meta:
        model = student
        fields = ['Amount_Paying','Staff_username']
