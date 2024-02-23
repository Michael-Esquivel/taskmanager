from django.contrib import admin
from .models import *

@admin.register(taskM)
class TaskM(admin.ModelAdmin):
    readonly_fields = ('created',)

