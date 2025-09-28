# realisations/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.realisations_liste, name="realisations_liste"),
]
