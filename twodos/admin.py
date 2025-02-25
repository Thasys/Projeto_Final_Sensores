from django.contrib import admin
from .models import SensorFisico


class SensorFisicoAdmin(admin.ModelAdmin):
    list_display = ("nome", "sigla", "tensao_min", "tensao_max")
    search_fields = ("nome", "sigla")


# Register your models here.
