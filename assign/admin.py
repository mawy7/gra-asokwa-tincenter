from django.contrib import admin
from .models import Assign


class AssignAdmin(admin.ModelAdmin):
    list_display = ("date_assigned", "staff_name", "office", "due_date", "no_of_assigned_task", "supervisor_remark", "time_of_completion")
    list_filter = ("date_assigned", "no_of_assigned_task", "due_date")

admin.site.register(Assign, AssignAdmin)