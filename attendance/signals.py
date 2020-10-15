from django.db.models.signals import post_save,post_delete,pre_delete,pre_save
from django.dispatch import receiver
from attendance.models import attendance
from users.models import profile
import os
import shutil
import json

@receiver(post_save, sender=profile)
def create_attendance(sender, instance, created, **kwargs):
   if created:
        with open('month.json') as f:
            data = json.load(f)
        attendance.objects.create(user_profile=instance,Absent=data)

@receiver(post_save, sender=profile)
def save_attendance(sender, instance, **kwargs):
    instance.attendance.save()