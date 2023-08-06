import os
from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
from schools.models import institutes
from users.models import Users
# from users.models import profile

POST = (
    ("","--------"),
    ("teacher","teacher"),
    ("lab Technician","Lab Technician"),
)

class teachers(models.Model):
    user = models.OneToOneField(Users,on_delete=models.CASCADE,null=True)
    # profile_user = models.OneToOneField(profile,on_delete=models.CASCADE,null=True)
    Faculty_ID = models.IntegerField(blank=False)
    Post = models.CharField(choices=POST,blank=False,max_length=20)
    Experiance = models.CharField(blank=False,max_length=20,default = "New to this profession")
    Subject = ArrayField(models.CharField(max_length=50), blank=True)
    Qualifications = ArrayField(models.CharField(max_length=200), blank=True)
    Spacility = ArrayField(models.CharField(max_length=100), blank=True)
    is_classteacher = models.BooleanField(blank=True,default=False)
    Class = models.CharField(blank=True,max_length=5)
    Section = models.CharField(blank=True,max_length=5)
    is_cordinator = models.BooleanField(blank=True,default=False)
    Cordinator = models.CharField(blank=True,max_length=50)
    institute = models.ForeignKey(institutes,on_delete=models.CASCADE,null=True)
    
    def __str__(self):
        return f'{self.Faculty_ID}_{self.user.username}'

#     # activities - classteacher
#     # acadaimics
