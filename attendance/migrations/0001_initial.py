# Generated by Django 2.1.2 on 2018-10-22 08:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AttendanceRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('present', 'Present'), ('unexcused', 'Unexcused'), ('excused', 'Excused'), ('late', 'Late')], max_length=10, verbose_name='')),
            ],
        ),
        migrations.CreateModel(
            name='Meeting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('date', models.DateField(verbose_name='Date')),
            ],
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Name')),
                ('admin', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='admin_of_set', to=settings.AUTH_USER_MODEL)),
                ('members', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='meeting',
            name='organization',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='attendance.Organization'),
        ),
        migrations.AddField(
            model_name='attendancerecord',
            name='meeting',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='attendance.Meeting'),
        ),
        migrations.AddField(
            model_name='attendancerecord',
            name='user',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]