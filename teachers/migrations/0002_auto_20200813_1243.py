# Generated by Django 3.0.8 on 2020-08-13 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='teachers',
            name='Class',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='teachers',
            name='Cordinator',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='teachers',
            name='Section',
            field=models.CharField(blank=True, max_length=5),
        ),
        migrations.AddField(
            model_name='teachers',
            name='is_classteacher',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AddField(
            model_name='teachers',
            name='is_cordinator',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]
