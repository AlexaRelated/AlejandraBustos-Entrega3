from django.apps import AppConfig

class InicioConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'inicio'

    def ready(self):
        # No realizar consultas a la base de datos
        pass

