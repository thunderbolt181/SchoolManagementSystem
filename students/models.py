import os
from django.db import models
from django.contrib.auth.models import User

CLASS = (
    ("1","1"),
    ("2","2"),
    ("3","3"),
    ("4","4"),
    ("5","5"),
    ("6","6"),
    ("7","7"),
    ("8","8"),
    ("9","9"),
    ("10","10"),
    ("11","11"),
    ("12","12")
)

class student(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    Admission_no = models.IntegerField(blank=False)
    Class = models.CharField(max_length=2,choices=CLASS,blank=False)
    Section = models.CharField(max_length=2,blank=False)
    Note_about_Student = models.TextField(max_length=500,blank=True)
    # remaning_fees = models.IntegerField(blank=False,default=-1)
    # Aadhar_Card = models.ImageField(default='default.jpg',blank=False,upload_to=path_and_rename)
    # Marksheet_10th = models.ImageField(default='default.jpg',blank=False,upload_to=path_and_rename)
    # Marksheet_12th = models.ImageField(default='default.jpg',blank=False,upload_to=path_and_rename)
    # Caste_Certificate = models.ImageField(default='default.jpg',blank=False,upload_to=path_and_rename)

    def __str__(self):
        return f"{self.user.profile.institute.id}_{self.Admission_no}_{self.user.first_name}_{self.user.last_name}"
