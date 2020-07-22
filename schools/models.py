from django.db import models
from PIL import Image
import os

def path_and_rename(instance, filename):
    upload_to = f'{instance.id}_{instance.Name}/'
    return os.path.join(upload_to, filename)

class institutes(models.Model):
    name = models.CharField(blank=False,max_length=150)
    address = models.TextField(blank=False)
    phone = models.IntegerField(blank=False)
    phone_other = models.IntegerField(blank=True)
    
    logo = models.ImageField(default='default.jpg',blank=False,upload_to=path_and_rename)

    def __str__(self):
        return self.Name