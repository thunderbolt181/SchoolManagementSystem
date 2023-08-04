# Generated by Django 4.2.3 on 2023-08-01 23:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('schools', '0001_initial'),
        ('users', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Admission_no', models.IntegerField()),
                ('Class', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'), ('11', '11'), ('12', '12')], max_length=2)),
                ('Section', models.CharField(max_length=2)),
                ('Roll_no', models.IntegerField()),
                ('Note_about_Student', models.TextField(blank=True, max_length=500)),
                ('institute', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='schools.institutes')),
                ('profile_user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.profile')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
