from django.contrib import admin
from .models import Task, Comment

# Register your models here.


class TaskAdmin(admin.ModelAdmin):
    readonly_fields = ('created', )


admin.site.register(Task, TaskAdmin)
admin.site.register(Comment)
