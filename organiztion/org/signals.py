from django.db.models.signals import post_migrate
from django.dispatch import receiver

@receiver(post_migrate)
def create_default_roles(sender, **kwargs):
    from .models import Role  
    # Your logic to create default roles
    if not Role.objects.exists():
        Role.objects.create(name='Admin')
        Role.objects.create(name='Editor')
        Role.objects.create(name='Viewer')