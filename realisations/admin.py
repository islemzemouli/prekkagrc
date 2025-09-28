from django.contrib import admin
from .models import Realisation


@admin.register(Realisation)
class RealisationAdmin(admin.ModelAdmin):
    list_display = ('titre', 'categorie', 'est_large', 'est_long')
    search_fields = ('titre', 'categorie', 'texte_alt')
    list_filter = ('categorie',)
