# Generated by Django 3.0.8 on 2020-07-06 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='Edit_Student_Detail',
            field=models.BooleanField(default=False),
        ),
    ]
