from django.db import models
from django.shortcuts import render
import datetime
from datetime import date
from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from django.urls import reverse
from django.conf import settings
from django.contrib.auth.models import User
from django.utils import timezone



class Organization(models.Model):
    name = models.CharField(max_length=50)
    city = models.CharField(default="", max_length=20)

    def __str__(self):
        return self.name



class Entry(models.Model):
    created_date = models.DateField(default=date.today, blank=True, null=True)
    organization = models.ForeignKey(Organization, null=True, blank=True, help_text="What is the name of the Organization", related_name="Organization", default='', on_delete=models.CASCADE)
    number = models.CharField(max_length=10)
    recieved_from = models.CharField(max_length=60, default="")
    contact_number = models.CharField(max_length=16, blank=False, null=True)
    recieving_officer = models.ForeignKey(settings.AUTH_USER_MODEL, blank=False, null=True, related_name='officer_recieving_files', on_delete=models.CASCADE)
    time_of_completion = models.DateField(default="YYYY-MM-DD", blank=True, null=True, help_text="Format ( YYYY-MM-DD ) Enter a date between now and 4 weeks (default 1).")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="Entry", default='', on_delete=models.CASCADE)

    class Meta:
        managed = True

    def __str__(self):
        return str(self.created_date)


class Dispatch(models.Model):
   
    STATUS = (('NS', 'Not Started'),
              ('IP', 'In Progress'),
              ('F', 'Finished'),
              ('OH', 'On Hold'),)
    dispatch_date = models.DateField(default=date.today, blank=True, null=True)
    organization = models.ForeignKey(Organization, default="", on_delete=models.CASCADE)
    complete = models.BooleanField(default=False)
    dispatching_officer = models.ForeignKey(
        settings.AUTH_USER_MODEL, blank=True, null=True, related_name='officer_dispatching_files', on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
    number_rejected = models.CharField(max_length=10)
    number_accepted = models.CharField(max_length=10)
    status = models.CharField(choices=STATUS, max_length=2, default='NS')
    dispatched_to = models.CharField(max_length=60)

    class Meta:
        managed = True

    def __str__(self):
        return str(self.dispatch_date)



def natural_key(self):
    return self.OrganizationName

    objects = OrganizationManager()

class OrganizationManager(models.Manager):

    def get_by_natural_key(self, name):
        return self.get(OrganizationName=name)