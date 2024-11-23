from django.contrib import admin

# Register your models here.
from .models import Organization, CustomUser, Role

admin.site.register(Organization)
admin.site.register(CustomUser)
admin.site.register(Role)
