# Generated by Django 2.0.1 on 2018-10-09 12:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Assign',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_assigned', models.DateField(blank=True, default=django.utils.timezone.now, null=True)),
                ('no_of_assigned_task', models.CharField(max_length=10)),
                ('office', models.CharField(help_text='What is the name of the Office', max_length=100)),
                ('due_date', models.DateField(blank=True, default='', null=True)),
                ('time_of_completion', models.DateField(blank=True, default='', null=True)),
                ('supervisor_remark', models.TextField(blank=True)),
                ('staff_name', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='User', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
