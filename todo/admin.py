from django.contrib import admin
from todo.models import Task, TaskList, Comment


class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'task_list', 'created_date', 'due_date', 'no_of_assigned_task', 'completed', 'completed_date', 'created_by', 'assigned_to', 'organization', 'time_of_completion', 'supervisor_remark', 'priority')
    list_filter = ('created_date', 'task_list',)
    ordering = ('priority',)
    search_fields = ('name',)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'date', 'snippet')


admin.site.register(TaskList)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Task, TaskAdmin)
