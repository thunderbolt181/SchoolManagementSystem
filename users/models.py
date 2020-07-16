from django.db import models
from django.contrib.auth.models import User

class profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    accoutant = models.BooleanField(default=False)
    Create_New_Entry = models.BooleanField(default=False)
    Edit_Student_Detail = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
