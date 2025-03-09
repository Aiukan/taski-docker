"""Сериализаторы приложения API проекта Taski."""
from rest_framework import serializers

from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    """Сериализатор модели Task приложения API."""

    class Meta:
        """Метаинформация сериализатора модели Task."""

        model = Task
        fields = ('id', 'title', 'description', 'completed')
