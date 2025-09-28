from django.shortcuts import render


def contact(request):
    """Affiche la page contact"""
    return render(request, "contact/contact.html")
