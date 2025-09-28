from django.db import models
from django.utils.text import slugify


class Service(models.Model):
    titre = models.CharField("Titre du service", max_length=200)
    slug = models.SlugField("URL optimisée", unique=True, blank=True)
    description = models.TextField("Description détaillée")
    image = models.ImageField("Image principale", upload_to="services/")
    meta_titre = models.CharField(
        "Titre SEO", max_length=255, blank=True, null=True)
    meta_description = models.TextField(
        "Description SEO", blank=True, null=True)
    date_creation = models.DateTimeField("Date de création", auto_now_add=True)
    date_mise_a_jour = models.DateTimeField(
        "Date de mise à jour", auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.titre)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.titre

    class Meta:
        ordering = ["titre"]
        verbose_name = "Service"
        verbose_name_plural = "Services"
