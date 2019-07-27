from django.contrib import admin
from health.models import Staff
from django.contrib.auth.admin import UserAdmin

# Register your models here.
admin.site.register(Staff)
