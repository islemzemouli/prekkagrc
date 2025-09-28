from django.db import models


class Realisation(models.Model):
    CATEGORIES = [
        ('photo', 'Photographie'),
        ('design', 'Design'),
        ('identite', 'Identité'),
        ('corporate', 'Corporate'),
        ('uxui', 'UI/UX'),
    ]

    titre = models.CharField(
        max_length=200, verbose_name="Titre de la réalisation"
    )
    image = models.ImageField(
        upload_to='realisations/', verbose_name="Image de la réalisation"
    )
    texte_alt = models.CharField(
        max_length=255, blank=True, verbose_name="Texte ALT (SEO)"
    )
    categorie = models.CharField(
        max_length=50, choices=CATEGORIES, verbose_name="Catégorie"
    )
    est_large = models.BooleanField(
        default=False, verbose_name="Large (grid-wide)"
    )
    est_long = models.BooleanField(
        default=False, verbose_name="Long (grid-long)"
    )

    def __str__(self):
        return self.titre

    def save(self, *args, **kwargs):
        # si ALT vide, on le remplit automatiquement avec le titre (bon fallback SEO)
        if not self.texte_alt:
            self.texte_alt = self.titre
        super().save(*args, **kwargs)
