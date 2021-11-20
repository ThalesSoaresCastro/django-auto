from django.apps import AppConfig


class UserapiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'userapi'

    def ready(self):
        from userapi.tools import filescheduler
        filescheduler.start_job()
