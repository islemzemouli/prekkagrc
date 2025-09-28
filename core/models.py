from django.db import models


class Carausel(models.Model):
    image = models.ImageField("Image", upload_to='pics/%y/%m/%d')
    title = models.CharField("Titre", max_length=150)
    cta = models.CharField("Texte du bouton", max_length=100)
    cta_link = models.URLField("Lien du bouton", default="/")

    def __str__(self):
        return self.title


class SocialLink(models.Model):
    titre = models.CharField(
        max_length=20,
        help_text="Texte qui s'affiche au survol et texte alternatif"
    )
    url = models.URLField(
        help_text="Lien vers le réseau social"
    )
    icone = models.ImageField(
        upload_to='icones_reseaux/',
        help_text="Télécharger l'icône du réseau social"
    )

    def __str__(self):
        return self.titre


class Temoignage(models.Model):
    nom = models.CharField("Nom du client", max_length=100)
    role = models.CharField("Rôle du client", max_length=50, default="Client")
    avis = models.TextField("Avis du client")
    email = models.EmailField(
        "Email du client (facultatif)", blank=True, null=True)
    cree_le = models.DateTimeField("Date de création", auto_now_add=True)

    def __str__(self):
        return f"{self.nom} - {self.role}"
