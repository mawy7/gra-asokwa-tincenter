from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

import datetime
from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

from django.urls import reverse
from django.conf import settings
from django.utils import timezone

# Create your models here.

class Assign(models.Model):
	staff_name = models.ForeignKey(User, related_name="User", default='', on_delete=models.CASCADE)
	date_assigned = models.DateField(default=timezone.now, blank=True, null=True)
	due_date = models.DateField(default='', blank=True, null=True)
	no_of_assigned_task = models.CharField(max_length=10)
	office = models.CharField(  help_text="What is the name of the Office", max_length=100)
	time_of_completion = models.DateField(default='', blank=True, null=True)
	supervisor_remark = models.TextField(blank=True)
