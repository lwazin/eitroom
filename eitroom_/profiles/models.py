from django.db import models
from accounts.models import User

class manager(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'Manager - {self.user.name}'

class tenant(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    degree = models.SlugField(blank=True, max_length=100)
    university = models.SlugField(blank=True, max_length=100)

    def __str__(self):
        return f'Tenant - {self.user.name}'
