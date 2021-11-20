from django.apps import AppConfig


class ProductapiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'productapi'

    def ready(self):
        from productapi.tools import filescheduler
        filescheduler.start_job()