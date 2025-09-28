from django import forms
from .models import Temoignage


class FormulaireTemoignage(forms.ModelForm):
    class Meta:
        model = Temoignage
        fields = ['nom', 'role', 'avis', 'email']
        labels = {
            'nom': "Votre nom",
            'role': "Votre rôle",
            'avis': "Votre avis",
            'email': "Votre email (facultatif)"
        }
        widgets = {
            'nom': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Entrez votre nom'
            }),
            'role': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ex: Client'
            }),
            'avis': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Écrivez votre avis ici',
                'rows': 4
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Votre email (facultatif)'
            })
        }

    # Validation for the name field
    def clean_nom(self):
        nom = self.cleaned_data.get('nom')
        if len(nom) < 2:
            raise forms.ValidationError(
                "Le nom doit contenir au moins 2 caractères.")
        return nom

    # Validation for the testimonial content
    def clean_avis(self):
        avis = self.cleaned_data.get('avis')
        if len(avis) < 10:
            raise forms.ValidationError(
                "L'avis doit contenir au moins 10 caractères.")
        return avis
