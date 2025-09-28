from django.db import models
from django.utils.text import slugify
from django.urls import reverse


class Article(models.Model):
    titre = models.CharField("Titre", max_length=200)
    slug = models.SlugField("Slug", unique=True, blank=True)
    contenu = models.TextField("Contenu")
    extrait = models.TextField(
        "Extrait", blank=True, help_text="Résumé court pour la page liste"
    )
    categorie = models.CharField("Catégorie", max_length=100, blank=True)
    image = models.ImageField(
        "Image", upload_to="blog_images/", blank=True, null=True)
    date_creation = models.DateTimeField("Date de création", auto_now_add=True)
    date_modification = models.DateTimeField(
        "Date de modification", auto_now=True)
    publie = models.BooleanField("Publié", default=True)

    class Meta:
        ordering = ['-date_creation']
        verbose_name = "Article"
        verbose_name_plural = "Articles"

    def save(self, *args, **kwargs):
        # Generate a unique slug if empty
        if not self.slug:
            base_slug = slugify(self.titre)
            slug = base_slug
            compteur = 1
            while Article.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{compteur}"
                compteur += 1
            self.slug = slug
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('blog:detail_article', kwargs={'slug': self.slug})

    def __str__(self):
        return self.titre
