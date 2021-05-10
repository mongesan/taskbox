from django.contrib import admin
from main.models import Task


class TaskAdmin(admin.ModelAdmin):
    list_display = ('name', 'comment', 'stat', 'stat_max', 'deadline', 'created_at',)
    list_display_links = ('name', 'comment', 'stat', 'stat_max', 'deadline',)


admin.site.register(Task, TaskAdmin)
