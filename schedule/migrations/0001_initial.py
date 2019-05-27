# Generated by Django 2.1.2 on 2018-10-22 08:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Calendar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='name')),
                ('slug', models.SlugField(max_length=200, unique=True, verbose_name='slug')),
            ],
            options={
                'verbose_name': 'calendar',
                'verbose_name_plural': 'calendars',
            },
        ),
        migrations.CreateModel(
            name='CalendarRelation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.IntegerField(db_index=True)),
                ('distinction', models.CharField(max_length=20, verbose_name='distinction')),
                ('inheritable', models.BooleanField(default=True, verbose_name='inheritable')),
                ('calendar', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schedule.Calendar', verbose_name='calendar')),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
            ],
            options={
                'verbose_name': 'calendar relation',
                'verbose_name_plural': 'calendar relations',
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.DateTimeField(db_index=True, verbose_name='start')),
                ('end', models.DateTimeField(db_index=True, help_text='The end time must be later than the start time.', verbose_name='end')),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('description', models.TextField(blank=True, verbose_name='description')),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='created on')),
                ('updated_on', models.DateTimeField(auto_now=True, verbose_name='updated on')),
                ('end_recurring_period', models.DateTimeField(blank=True, db_index=True, help_text='This date is ignored for one time only events.', null=True, verbose_name='end recurring period')),
                ('color_event', models.CharField(blank=True, max_length=10, verbose_name='Color event')),
                ('calendar', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schedule.Calendar', verbose_name='calendar')),
                ('creator', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='creator', to=settings.AUTH_USER_MODEL, verbose_name='creator')),
            ],
            options={
                'verbose_name': 'event',
                'verbose_name_plural': 'events',
            },
        ),
        migrations.CreateModel(
            name='EventRelation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.IntegerField(db_index=True)),
                ('distinction', models.CharField(max_length=20, verbose_name='distinction')),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schedule.Event', verbose_name='event')),
            ],
            options={
                'verbose_name': 'event relation',
                'verbose_name_plural': 'event relations',
            },
        ),
        migrations.CreateModel(
            name='Occurrence',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, verbose_name='title')),
                ('description', models.TextField(blank=True, verbose_name='description')),
                ('start', models.DateTimeField(db_index=True, verbose_name='start')),
                ('end', models.DateTimeField(db_index=True, verbose_name='end')),
                ('cancelled', models.BooleanField(default=False, verbose_name='cancelled')),
                ('original_start', models.DateTimeField(verbose_name='original start')),
                ('original_end', models.DateTimeField(verbose_name='original end')),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='created on')),
                ('updated_on', models.DateTimeField(auto_now=True, verbose_name='updated on')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schedule.Event', verbose_name='event')),
            ],
            options={
                'verbose_name': 'occurrence',
                'verbose_name_plural': 'occurrences',
            },
        ),
        migrations.CreateModel(
            name='Rule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='name')),
                ('description', models.TextField(verbose_name='description')),
                ('frequency', models.CharField(choices=[('YEARLY', 'Yearly'), ('MONTHLY', 'Monthly'), ('WEEKLY', 'Weekly'), ('DAILY', 'Daily'), ('HOURLY', 'Hourly'), ('MINUTELY', 'Minutely'), ('SECONDLY', 'Secondly')], max_length=10, verbose_name='frequency')),
                ('params', models.TextField(blank=True, verbose_name='params')),
            ],
            options={
                'verbose_name': 'rule',
                'verbose_name_plural': 'rules',
            },
        ),
        migrations.AddField(
            model_name='event',
            name='rule',
            field=models.ForeignKey(blank=True, help_text="Select '----' for a one time only event.", null=True, on_delete=django.db.models.deletion.CASCADE, to='schedule.Rule', verbose_name='rule'),
        ),
        migrations.AlterIndexTogether(
            name='occurrence',
            index_together={('start', 'end')},
        ),
        migrations.AlterIndexTogether(
            name='eventrelation',
            index_together={('content_type', 'object_id')},
        ),
        migrations.AlterIndexTogether(
            name='event',
            index_together={('start', 'end')},
        ),
        migrations.AlterIndexTogether(
            name='calendarrelation',
            index_together={('content_type', 'object_id')},
        ),
    ]
