from django.apps import AppConfig


class LoggerConfig(AppConfig):
    name = 'logger'

    def ready(self):
        import logger.signals
