"""Настройка админ-зоны API приложения Taski."""
from django.contrib import admin

from .models import Task


class TaskAdmin(admin.ModelAdmin):
    """Представление объекта Task в админ-зоне."""

    list_display = ('title', 'description', 'completed')


admin.site.register(Task, TaskAdmin)
