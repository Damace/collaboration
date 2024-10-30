from django.apps import AppConfig


class SystemusersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'systemUsers'

    def ready(self):
        import systemUsers.signals  # Ensure signals are imported