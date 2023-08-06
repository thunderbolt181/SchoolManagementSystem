from django.db import models
from PIL import Image
import os
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
from users.models import Users
# from users.models import profile

def path_and_rename(instance, filename):
    upload_to = f'{instance.id}/'
    return os.path.join(upload_to, filename)

class institutes(models.Model):
    Name = models.CharField(blank=False,max_length=150)
    Address = models.TextField(blank=False)
    Contact_Phone_1 = models.CharField(blank=False,max_length=10)
    Contact_Phone_2 = models.CharField(blank=True,max_length=10)
    Contact_Email = models.EmailField(blank=True)
    logo = models.ImageField(default='default.jpg',blank=False,upload_to=path_and_rename)

    def save(self, *args, **kwargs):
        super().save()
        try :
            img=Image.open(self.logo.path)
            if img.height > 512 or img.width > 512:
                new_img = (512,512)
                img.thumbnail(new_img)
                img.save(self.logo.path)
        except:
            pass

    def __str__(self):
        return self.Name

POST=(
    ('director','Director'),
    ('principal','Principal'),
    ('vice principal','Vice Principal'),
    ('accountant','Accountant'),
    ('receptionist','Receptionist'),
    ('editor','Admin Editor(Have all kind of Permissions)'),
)

class staff(models.Model):
    # user = models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    user = models.OneToOneField(Users,on_delete=models.CASCADE,null=True)
    # profile_user = models.OneToOneField(profile,on_delete=models.CASCADE,null=True)
    institute = models.ForeignKey(institutes,on_delete=models.CASCADE,null=True)
    Staff_ID = models.IntegerField(blank=False)
    Post = models.CharField(choices=POST,blank=False,max_length=20)

    def __str__(self):
        return f"{self.Staff_ID}_{self.user.first_name} {self.user.last_name}"