from django.contrib import admin
from task_app.models.status import Status
from task_app.models.type import Type
from task_app.models.task import Task


class StatusAdmin(admin.ModelAdmin):
    list_display = ('id', 'status')
    list_filter = ('id', 'status')
    search_field = ('id', 'status')
    fields = ('status',)


class TypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'type')
    list_filter = ('id', 'type')
    search_field = ('id', 'type')
    fields = ('type',)


class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'task', 'status', 'type', 'created_at', 'changed_at')
    list_filter = ('id', 'task', 'status', 'type', 'created_at', 'changed_at')
    search_field = ('task', 'status', 'type', 'created_at', 'changed_at')
    fields = ('task', 'description', 'status', 'typec')



admin.site.register(Status, StatusAdmin)
admin.site.register(Type, TypeAdmin)
admin.site.register(Task, TaskAdmin)