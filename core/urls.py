from django.urls import path
from . import views

urlpatterns = [
    path('', views.accueil, name='accueil'),
    # make sure view name matches
    # <--- must match view function
    path('apropos/', views.apropos, name='apropos'),
    path('ajouter-temoignage/', views.ajouter_temoignage,
         name='ajouter_temoignage'),  # Form page to submit a testimonial

]
