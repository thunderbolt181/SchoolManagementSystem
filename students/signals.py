from django.utils.text import slugify
from django.dispatch import receiver
from django.db import models
from .models import student
import os

@receiver(models.signals.pre_save, sender=student)
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

    try:
        old_file = sender.objects.get(pk=instance.pk).Marksheet_10th
        new_file = instance.Marksheet_10th
        if not old_file == new_file:
            if os.path.isfile(old_file.path) and old_file.path.split("\\")[-1] != 'default.jpg':
                print(old_file.path)
                os.remove(old_file.path)
    except sender.DoesNotExist:
        return False

    try:
        old_file = sender.objects.get(pk=instance.pk).Marksheet_12th
        new_file = instance.Marksheet_12th
        if not old_file == new_file and old_file.path.split("\\")[-1] != 'default.jpg':
            if os.path.isfile(old_file.path):
                os.remove(old_file.path)
    except sender.DoesNotExist:
        return False

    try:
        old_file = sender.objects.get(pk=instance.pk).Caste_Certificate
        new_file = instance.Caste_Certificate
        if not old_file == new_file:
            if os.path.isfile(old_file.path) and old_file.path.split("\\")[-1] != 'default.jpg':
                os.remove(old_file.path)
    except sender.DoesNotExist:
        return False

    try:
        old_file = sender.objects.get(pk=instance.pk).Aadhar_Card
        new_file = instance.Aadhar_Card
        if not old_file == new_file:
            if os.path.isfile(old_file.path) and old_file.path.split("\\")[-1] != 'default.jpg':
                os.remove(old_file.path)
    except sender.DoesNotExist:
        return False