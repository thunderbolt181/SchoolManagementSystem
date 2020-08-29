from django.contrib.auth.models import User
from django.db.models.signals import post_save,post_delete,pre_delete,pre_save
from django.dispatch import receiver
from users.models import profile
from django.utils.text import slugify
from django.db import models
import os
import shutil

# @receiver(post_save, sender=User)
# def create_profile(sender, instance, created, **kwargs):
#     if created:
#         profile.objects.create(user=instance)

# @receiver(post_save, sender=User)
# def save_profile(sender, instance, **kwargs):
#     instance.profile.save()

@receiver(post_delete, sender=profile)
def auto_delete_user_with_profile(sender, instance, **kwargs):
    instance.user.delete()

@receiver(pre_delete, sender=profile)
def auto_delete_profile_pic_with_profile(sender, instance, **kwargs):
    path = os.path.split(instance.Profile_pic.path)[0]
    shutil.rmtree(path, ignore_errors=True)

@receiver(pre_save, sender=profile)
def auto_delete_file_on_change(sender, instance, **kwargs):
    if not instance.pk:
        return False
    try:
        old_file = sender.objects.get(pk=instance.pk).Profile_pic
        new_file = instance.Profile_pic
        if not old_file == new_file:
            if os.path.isfile(old_file.path):
                os.remove(old_file.path)
    except sender.DoesNotExist:
        return False