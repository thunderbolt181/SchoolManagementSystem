from django.db.models.signals import post_save,post_delete,pre_delete,pre_save
from django.dispatch import receiver
from schools.models import institutes
import os
import shutil

@receiver(pre_save, sender=institutes)
def auto_delete_file_on_change(sender, instance, **kwargs):
    print("Accessing function")
    if not instance.pk:
        return False
    try:
        old_file = sender.objects.get(pk=instance.pk).logo
        new_file = instance.logo
        if not old_file == new_file:
            if os.path.isfile(old_file.path):
                os.remove(old_file.path)
    except sender.DoesNotExist:
        return False
    
@receiver(pre_delete, sender=institutes)
def auto_delete_logo_with_profile(sender, instance, **kwargs):
    print("Accessing function")
    path = os.path.split(instance.logo.path)[0]
    shutil.rmtree(path, ignore_errors=True)