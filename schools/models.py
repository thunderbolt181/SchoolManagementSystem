from django.db import models
from PIL import Image
import os

def path_and_rename(instance, filename):
    upload_to = f'{instance.id}_{instance.Name}/'
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