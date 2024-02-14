from django.apps import AppConfig


class MedconnectConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'medconnect'

    def ready(self):
        import medconnect.signals
