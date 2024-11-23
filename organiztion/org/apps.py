from django.apps import AppConfig
from django.db.models.signals import post_migrate
from .signals import create_default_roles

class OrgConfig(AppConfig):
    name = 'org'

    def ready(self):
        
        import org.signals