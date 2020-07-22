from django import forms
from students.models import student
from django.contrib.auth.models import User

class StudentCreateForm(forms.ModelForm):
    class Meta:
        model = student
        fields = ['Admission_no','Name','DOB','Gender','Email','Class','Aadhar_Number',
            'Fathers_Name','Fathers_Occupation','Mothers_Name','Mothers_Occupation',
            'Phone','Phone_Other','Relegion','caste','Category','Address','Nationality','Profile_pic','Aadhar_Card',"Marksheet_10th",
            "Marksheet_12th","Caste_Certificate",'Note_about_Student']

class submit_fees(forms.Form):
    Amount_Paying = forms.IntegerField()
    Staff_username = forms.CharField(max_length=100)

    class Meta:
        model = student
        fields = ['Amount_Paying','Staff_username']
