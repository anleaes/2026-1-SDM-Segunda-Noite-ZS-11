from django.apps import AppConfig

class PersonsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'persons'
    verbose_name = 'Pessoa'
    label = "gc_persons"
