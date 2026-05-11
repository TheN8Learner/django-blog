from django import forms
from .models import Commentaire, Contact

class commentaryMessage(forms.ModelForm):
    class Meta:
        model = Commentaire
        fields = ['auteur', 'texte']
        widgets = {
            'texte': forms.Textarea(attrs={
                'placeholder': 'Écrivez votre commentaire...',
                'rows': 4,
            })
        }

class contactMessage(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['nom', 'prenom', 'email', 'message']
        widgets = {
            'nom': forms.TextInput(attrs=
                                      {'placeholder': 'Entrer votre nomm...'}),
            'prenom': forms.TextInput(attrs=
                                      {'placeholder': 'Entrer votre prenom...'}),
            'email': forms.EmailInput(attrs=
                                      {'placeholder': 'Entrer votre email...'}),
            'message': forms.Textarea(attrs=
                                      {'placeholder': 'Entrer votre message...',
                                       'rows': 4})
        }