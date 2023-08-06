from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import shutil
from PIL import Image
import os
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

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
    upload_to = f"{instance.status}/{instance.username}"
    return os.path.join(upload_to, filename)

class MyUsersManager(BaseUserManager):
    def create_user(self, email, username, password = None):
        if not email:
            raise ValueError("Users must have an email address")
        if not username:
            raise ValueError("Users must have a username")
        
        user = self.model(
            email = self.normalize_email(email),
            username = username,
        )

        user.set_password(password)
        user.save(using = self._db)

        return user
    
    def create_superuser(self, email, username, password):
        user = self.create_user(
            email = self.normalize_email(email),
            username = username,
            password = password
        )

        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True

        user.save(using = self._db)

        return user

class Users(AbstractBaseUser):
    """
    - Creating custom user model.
    - using email to log in instead of username but username is still there.
    - username, date_joined, last_login, is_admin, is_active, is_superuser should
        be there in custom user model.
    """
    email               = models.EmailField(verbose_name='email',max_length=60,unique=True)
    username            = models.CharField(max_length=30,unique=True)
    date_join           = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login          = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin            = models.BooleanField(default=False)
    is_active           = models.BooleanField(default=True)
    is_staff            = models.BooleanField(default=False)
    is_superuser        = models.BooleanField(default=False)

    first_name          = models.CharField(verbose_name='first_name', max_length=20,default="")
    last_name           = models.CharField(verbose_name='last_name', max_length=20, default="")
    status              = models.CharField(choices=STATUS,default="",blank=False,max_length=10)
    DOB                 = models.DateField(blank=False,default=timezone.now)
    Gender              = models.CharField(max_length=10,choices=GENDER,blank=False,default="")
    phone_1             = models.CharField(max_length=10,blank=False,default='')
    phone_2             = models.CharField(max_length=10,default='')
    Aadhar_Number       = models.CharField(blank=True,default='',max_length=12)
    Fathers_Name        = models.CharField(max_length=100,blank=False,default="")
    Fathers_Occupation  = models.CharField(max_length=100,blank=True)
    Mothers_Name        = models.CharField(max_length=100,blank=False,default="")
    Mothers_Occupation  = models.CharField(max_length=100,blank=True)
    House_No            = models.CharField(blank=False,max_length=100,default='')
    Street_Name         = models.CharField(blank=False,max_length=100,default='')
    city                = models.CharField(blank=False,max_length=100,default='')
    PIN_Code            = models.CharField(blank=False,max_length=10,default='')
    Category            = models.CharField(max_length=20,choices=CATEGORY,blank=False,default="")
    Profile_pic         = models.ImageField(default='default.jpg',blank=False,upload_to=path_and_rename)

    USERNAME_FIELD = 'email' # set to username or email to change the login method.
    REQUIRED_FIELDS = ['username'] # can add custom fields also

    objects = MyUsersManager()

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

    def __str__(self) -> str:
        return self.email
    
    def has_perm(self, perm, obj = None):
        return self.is_admin
    
    def has_module_perms(self, app_label):
        return True

###########################################    IMPORTANT   #####################################################

# Do not show all of the student/teacher/staff of a institute using pagination 
# rather let the user make filter or search user specific keywords
# this will decrease the number items in the queryset and hence decreasing
# the load on Pagination object and hence making searching faster

################################################################################################################

# class profile(models.Model):
#     # user = models.OneToOneField(User,on_delete=models.CASCADE,null=True)
#     user = models.OneToOneField(Users,on_delete=models.CASCADE,null=True)
#     status = models.CharField(choices=STATUS,default="",blank=False,max_length=10)
#     DOB = models.DateField(blank=False,default=timezone.now)
#     Gender = models.CharField(max_length=10,choices=GENDER,blank=False,default="")
#     phone_1 = models.CharField(max_length=10,blank=False,default='')
#     phone_2 = models.CharField(max_length=10,default='')
#     Aadhar_Number = models.CharField(blank=True,default='',max_length=12)
#     Fathers_Name = models.CharField(max_length=100,blank=False,default="")
#     Fathers_Occupation = models.CharField(max_length=100,blank=True)
#     Mothers_Name = models.CharField(max_length=100,blank=False,default="")
#     Mothers_Occupation = models.CharField(max_length=100,blank=True)
#     House_No = models.CharField(blank=False,max_length=100,default='')
#     Street_Name = models.CharField(blank=False,max_length=100,default='')
#     city = models.CharField(blank=False,max_length=100,default='')
#     PIN_Code = models.CharField(blank=False,max_length=10,default='')
#     Category = models.CharField(max_length=20,choices=CATEGORY,blank=False,default="")
#     Profile_pic = models.ImageField(default='default.jpg',blank=False,upload_to=path_and_rename)

#     def save(self, *args, **kwargs):
#         super().save()
#         try :
#             img=Image.open(self.Profile_pic.path)
#             if img.height > 512 or img.width > 512:
#                 new_img = (512,512)
#                 img.thumbnail(new_img)
#                 img.save(self.Profile_pic.path)
#         except:
#             pass

#     def __str__(self):
#         return self.user.username
