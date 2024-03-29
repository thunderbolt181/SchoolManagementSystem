# Generated by Django 4.2.3 on 2023-08-05 08:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import schools.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='institutes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=150)),
                ('Address', models.TextField()),
                ('Contact_Phone_1', models.CharField(max_length=10)),
                ('Contact_Phone_2', models.CharField(blank=True, max_length=10)),
                ('Contact_Email', models.EmailField(blank=True, max_length=254)),
                ('logo', models.ImageField(default='default.jpg', upload_to=schools.models.path_and_rename)),
            ],
        ),
        migrations.CreateModel(
            name='staff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Staff_ID', models.IntegerField()),
                ('Post', models.CharField(choices=[('director', 'Director'), ('principal', 'Principal'), ('vice principal', 'Vice Principal'), ('accountant', 'Accountant'), ('receptionist', 'Receptionist'), ('editor', 'Admin Editor(Have all kind of Permissions)')], max_length=20)),
                ('institute', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='schools.institutes')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
