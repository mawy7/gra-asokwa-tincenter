# Generated by Django 2.1.2 on 2018-10-22 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entry', '0002_auto_20181022_0919'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='time_of_completion',
            field=models.DateField(blank=True, help_text='Format ( YYYY-MM-DD ) Enter a date between now and 4 weeks (default 1).', null=True),
        ),
    ]