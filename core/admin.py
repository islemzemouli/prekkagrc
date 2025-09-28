from django.contrib import admin
from .models import Carausel, SocialLink, Temoignage


@admin.register(Carausel)
class CarauselAdmin(admin.ModelAdmin):
    list_display = ("title", "cta", "cta_link")   # colonnes visibles
    search_fields = ("title", "cta")              # champ de recherche
    list_filter = ("title",)                      # filtre latéral


@admin.register(SocialLink)
class SocialLinkAdmin(admin.ModelAdmin):
    list_display = ('titre', 'url')          # Columns shown in admin list
    list_display_links = ('titre',)          # Make the title clickable
    search_fields = ('titre', 'url')         # Allow search by title or URL
    list_per_page = 20                        # Pagination


@admin.register(Temoignage)
class TemoignageAdmin(admin.ModelAdmin):
    list_display = ('nom', 'role', 'cree_le')
    search_fields = ('nom', 'role', 'avis', 'email')
    ordering = ('-cree_le',)
