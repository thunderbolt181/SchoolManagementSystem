from django.db import models
from django.contrib.auth.models import User
from schools.models import institutes

####### Before creating superuser ..... create a foo institute entry with id = 1 in Mysql workbench ........ 

STATUS=(
    ("","-----"),
    ("student","Student"),
    ("teacher","Teacher"),
    ("staff","Staff")
)

class profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    status = models.CharField(choices=STATUS,default="",blank=False,max_length=10)
    institute = models.ForeignKey(institutes,on_delete=models.CASCADE,blank=True,default=1)

    def __str__(self):
        return self.user.username
