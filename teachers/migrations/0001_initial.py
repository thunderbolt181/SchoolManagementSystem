# Generated by Django 4.2.3 on 2023-08-05 08:48

from django.conf import settings
import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('schools', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='teachers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Faculty_ID', models.IntegerField()),
                ('Post', models.CharField(choices=[('', '--------'), ('teacher', 'teacher'), ('lab Technician', 'Lab Technician')], max_length=20)),
                ('Experiance', models.CharField(default='New to this profession', max_length=20)),
                ('Subject', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=50), blank=True, size=None)),
                ('Qualifications', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), blank=True, size=None)),
                ('Spacility', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=100), blank=True, size=None)),
                ('is_classteacher', models.BooleanField(blank=True, default=False)),
                ('Class', models.CharField(blank=True, max_length=5)),
                ('Section', models.CharField(blank=True, max_length=5)),
                ('is_cordinator', models.BooleanField(blank=True, default=False)),
                ('Cordinator', models.CharField(blank=True, max_length=50)),
                ('institute', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='schools.institutes')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
