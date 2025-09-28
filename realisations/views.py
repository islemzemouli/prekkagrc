# realisations/views.py
from django.shortcuts import render
from .models import Realisation


def realisations_liste(request):
    """
    Vue qui affiche toutes les réalisations dans le portfolio.
    """
    realisations = Realisation.objects.all()
    return render(request, "realisations/realisations_liste.html", {
        "realisations": realisations
    })
