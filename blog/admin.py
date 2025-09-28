from django.contrib import admin
from .models import Article


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('titre', 'categorie', 'publie',
                    'date_creation', 'date_modification')
    list_filter = ('publie', 'categorie', 'date_creation', 'date_modification')
    search_fields = ('titre', 'contenu', 'extrait', 'categorie')
    prepopulated_fields = {'slug': ('titre',)}
    readonly_fields = ('date_creation', 'date_modification')

    fieldsets = (
        (None, {
            'fields': ('titre', 'slug', 'contenu', 'extrait', 'categorie', 'publie', 'image')
        }),
        ('Dates', {
            'fields': ('date_creation', 'date_modification')
        }),
    )
