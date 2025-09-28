from django.shortcuts import render
from .models import Carausel
from .forms import FormulaireTemoignage, Temoignage
from services.models import Service
from realisations.models import Realisation  # import Realisation model


def accueil(request):
    diapositives = Carausel.objects.all()
    services = Service.objects.all()[:3]

    # Get all realisations
    realisations = Realisation.objects.all()

    context = {
        "diapositives": diapositives,
        "services": services,
        "realisations": realisations,  # pass to template
    }
    return render(request, "core/accueil.html", context)


def apropos(request):
    return render(request, "core/apropos.html")


def ajouter_temoignage(request):
    """
    Handle testimonial submission from clients.
    """
    success = False
    error = False

    if request.method == 'POST':
        form = FormulaireTemoignage(request.POST)
        if form.is_valid():
            form.save()  # Save testimonial directly
            success = True
            form = FormulaireTemoignage()  # Clear form after submission
        else:
            error = True  # Form has validation errors
    else:
        form = FormulaireTemoignage()

    return render(request, 'core/ajouter_temoin.html', {
        'form': form,
        'success': success,
        'error': error
    })


def apropos(request):
    """
    Display all testimonials.
    """
    temoignages = Temoignage.objects.all().order_by('-cree_le')
    return render(request, 'core/apropos.html', {
        'temoignages': temoignages
    })
