from django.db import models
from users.models import Users
# from users.models import profile

class attendance(models.Model):
    user = models.OneToOneField(Users,on_delete=models.CASCADE,null=True)
    # user_profile = models.OneToOneField(profile,on_delete=models.CASCADE)
    Absent = models.JSONField(null = True,blank = True)

    def __str__(self):
        return f"{self.user.id}_{self.user.first_name} {self.user.last_name}"