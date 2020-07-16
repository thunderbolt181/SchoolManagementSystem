import os
import shutil
import eav
from PIL import Image
from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin


GENDER=(
    ("Male","Male"),
    ("Female","Female")
)

CATEGORY=(
    ("","Choice"),
    ("General","General"),
    ("OBC","OBC"),
    ("SC","SC"),
    ("ST","ST")
)

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

def path_and_rename(instance, filename):
    upload_to = f'student/{instance.Admission_no}_{instance.Name}/'
    return os.path.join(upload_to, filename)

class student(models.Model):
    Admission_no = models.IntegerField(default=00000,blank=False,unique=True)
    Name = models.CharField(max_length=100,blank=False)
    DOB = models.DateField(blank=False,default="YYYY-MM-DD")
    Gender =models.CharField(max_length=10,choices=GENDER,blank=False)
    Class = models.CharField(max_length=2,choices=CLASS,blank=False)
    Phone = models.IntegerField(blank=False)
    Phone_Other = models.IntegerField(default=0,blank=True)
    Email = models.EmailField(blank=True)
    Address = models.TextField(max_length=300,blank=False)
    Fathers_Name = models.CharField(max_length=100,blank=False)
    Fathers_Occupation = models.CharField(max_length=100,blank=True)
    Mothers_Name = models.CharField(max_length=100,blank=False)
    Mothers_Occupation = models.CharField(max_length=100,blank=True)
    Relegion = models.CharField(max_length=50,blank=False)
    caste = models.CharField(max_length=50,blank=False)
    Category = models.CharField(max_length=20,choices=CATEGORY,blank=False,default="")
    Nationality = models.CharField(max_length=50,blank=False,default="Indian")
    Note_about_Student = models.TextField(max_length=500,blank=True)
    created_on = models.DateField(auto_now_add=True)
    created_by = models.ForeignKey(User,null=True,on_delete=models.SET_NULL)
    remaning_fees = models.IntegerField(blank=False,default=-1)
    paid_fees = models.IntegerField(blank=False,default=0)
    Aadhar_Number = models.IntegerField(blank=False,default=0)
    Profile_pic = models.ImageField(blank=False,upload_to=path_and_rename)
    Aadhar_Card = models.ImageField(default='default.jpg',blank=False,upload_to=path_and_rename)
    Marksheet_10th = models.ImageField(default='default.jpg',blank=False,upload_to=path_and_rename)
    Marksheet_12th = models.ImageField(default='default.jpg',blank=False,upload_to=path_and_rename)
    Caste_Certificate = models.ImageField(default='default.jpg',blank=False,upload_to=path_and_rename)

    def delete(self, *args, **kwargs):
        path=f"media/student/{self.Admission_no}_{self.Name}"
        shutil.rmtree(path)
        print("*"*50)
        super().delete(*args,**kwargs)

    def save(self, *args, **kwargs):
        super().save()
        try :
            img=Image.open(self.Profile_pic.path)
            if img.height > 512 or img.width > 512:
                new_img = (512,512)
                img.thumbnail(new_img)
                img.save(self.Profile_pic.path)
        except:
            pass

    def __str__(self):
        return self.Name

eav.register(student)