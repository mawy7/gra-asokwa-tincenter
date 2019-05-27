from django.contrib import admin
from .models import Entry, Organization, Dispatch


class OrganizationAdmin(admin.ModelAdmin):
    list_display = ("name", "city")
    list_filter = ("name", "city")


class EntryAdmin(admin.ModelAdmin):
    list_display = ("created_date", "user", "organization", "recieved_from", "recieving_officer")
    list_filter = ("organization", "time_of_completion")


class DispatchAdmin(admin.ModelAdmin):
    list_display = ("dispatch_date", "organization", "status", "dispatched_to")
    list_filter = ("status", "dispatched_to")



admin.site.register(Organization, OrganizationAdmin)
admin.site.register(Entry, EntryAdmin)
admin.site.register(Dispatch, DispatchAdmin)