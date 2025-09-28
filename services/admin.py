from django.contrib import admin
from .models import Service


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("titre", "slug", "date_creation", "date_mise_a_jour")
    search_fields = ("titre", "description")
    prepopulated_fields = {"slug": ("titre",)}
