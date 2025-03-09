"""Настройки приложения API проекта Taski."""
from django.apps import AppConfig


class ApiConfig(AppConfig):
    """Конфиг приложения API проекта Taski."""

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'
