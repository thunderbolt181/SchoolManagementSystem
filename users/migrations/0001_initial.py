# Generated by Django 3.0.8 on 2020-08-10 13:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import users.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('schools', '0002_staff'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('', '-----'), ('student', 'Student'), ('teacher', 'Teacher'), ('staff', 'Staff')], default='', max_length=10)),
                ('DOB', models.DateField(default=django.utils.timezone.now)),
                ('Gender', models.CharField(choices=[('', '------'), ('Male', 'Male'), ('Female', 'Female')], default='', max_length=10)),
                ('phone_1', models.CharField(default='', max_length=10)),
                ('phone_2', models.CharField(default='', max_length=10)),
                ('Aadhar_Number', models.CharField(blank=True, default='', max_length=12)),
                ('Fathers_Name', models.CharField(default='', max_length=100)),
                ('Fathers_Occupation', models.CharField(blank=True, max_length=100)),
                ('Mothers_Name', models.CharField(default='', max_length=100)),
                ('Mothers_Occupation', models.CharField(blank=True, max_length=100)),
                ('House_No', models.CharField(default='', max_length=100)),
                ('Street_Name', models.CharField(default='', max_length=100)),
                ('city', models.CharField(default='', max_length=100)),
                ('PIN_Code', models.CharField(default='', max_length=10)),
                ('Category', models.CharField(choices=[('', '------'), ('General', 'General'), ('OBC', 'OBC'), ('SC', 'SC'), ('ST', 'ST')], default='', max_length=20)),
                ('Profile_pic', models.ImageField(default='default.jpg', upload_to=users.models.path_and_rename)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
