from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import shutil
from PIL import Image
import os

####### Before creating superuser ..... create a foo institute entry with id = 1 via PgAdmin4 in schools_institute table ........ 


###########################################    IMPORTANT   #####################################################

# Do not show all of the student/teacher/staff of a institute using pagination 
# rather let the user make filter or search user specific keywords
# this will decrease the number items in the queryset and hence decreasing
# the load on Pagination object and hence making searching faster

################################################################################################################

CATEGORY=(
    ("","------"),
    ("General","General"),
    ("OBC","OBC"),
    ("SC","SC"),
    ("ST","ST")
)

GENDER=(
    ("","------"),
    ("Male","Male"),
    ("Female","Female")
)

STATUS=(
    ("","-----"),
    ("student","Student"),
    ("teacher","Teacher"),
    ("staff","Staff")
)

def path_and_rename(instance, filename):
    upload_to = f"{instance.status}/{instance.user.username}"
    return os.path.join(upload_to, filename)

class profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    status = models.CharField(choices=STATUS,default="",blank=False,max_length=10)
    DOB = models.DateField(blank=False,default=timezone.now)
    Gender = models.CharField(max_length=10,choices=GENDER,blank=False,default="")
    phone_1 = models.CharField(max_length=10,blank=False,default='')
    phone_2 = models.CharField(max_length=10,default='')
    Aadhar_Number = models.CharField(blank=True,default='',max_length=12)
    Fathers_Name = models.CharField(max_length=100,blank=False,default="")
    Fathers_Occupation = models.CharField(max_length=100,blank=True)
    Mothers_Name = models.CharField(max_length=100,blank=False,default="")
    Mothers_Occupation = models.CharField(max_length=100,blank=True)
    House_No = models.CharField(blank=False,max_length=100,default='')
    Street_Name = models.CharField(blank=False,max_length=100,default='')
    city = models.CharField(blank=False,max_length=100,default='')
    PIN_Code = models.CharField(blank=False,max_length=10,default='')
    Category = models.CharField(max_length=20,choices=CATEGORY,blank=False,default="")
    Profile_pic = models.ImageField(default='default.jpg',blank=False,upload_to=path_and_rename)

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
        return self.user.username
