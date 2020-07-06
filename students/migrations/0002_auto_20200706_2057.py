# Generated by Django 3.0.8 on 2020-07-06 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='MOthers_Occupation',
            new_name='Mothers_Occupation',
        ),
        migrations.AddField(
            model_name='student',
            name='Admission_no',
            field=models.IntegerField(default=0, unique=True),
        ),
        migrations.AddField(
            model_name='student',
            name='Category',
            field=models.CharField(choices=[('General', 'General'), ('OBC', 'OBC'), ('SC', 'SC'), ('ST', 'ST')], default='', max_length=20),
        ),
        migrations.AddField(
            model_name='student',
            name='Email',
            field=models.EmailField(blank=True, max_length=254),
        ),
        migrations.AddField(
            model_name='student',
            name='paid_fees',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='student',
            name='remaning_fees',
            field=models.IntegerField(default=-1),
        ),
        migrations.AlterField(
            model_name='student',
            name='DOB',
            field=models.DateField(default='YYYY-MM-DD'),
        ),
        migrations.AlterField(
            model_name='student',
            name='Phone',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='student',
            name='Phone_Other',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
