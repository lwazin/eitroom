from django.contrib import admin
from .models import manager, tenant

admin.site.register(manager)
admin.site.register(tenant)
