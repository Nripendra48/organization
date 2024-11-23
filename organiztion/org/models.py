from django.contrib.auth.models import AbstractUser
from django.db import models


class Organization(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()
    is_main = models.BooleanField(default=False)  # Identify the main organization

    def __str__(self):
        return self.name


class CustomUser(AbstractUser):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name='users', null=True, blank=True)
    roles = models.ManyToManyField('Role', blank=True)

    def __str__(self):
        return self.username


class Role(models.Model):
    name = models.CharField(max_length=100, unique=True)  # e.g., "Admin", "Editor", "Viewer"

    def __str__(self):
        return self.name