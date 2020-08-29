from django.db import models
from users.models import profile

class attendance(models.Model):
    user_profile = models.OneToOneField(profile,on_delete=models.CASCADE)
    Absent = models.JSONField(null = True,blank = True)

    def __str__(self):
        return f"{self.user_profile.id}_{self.user_profile.user.first_name} {self.user_profile.user.last_name}"