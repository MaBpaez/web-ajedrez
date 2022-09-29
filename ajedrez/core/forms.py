from django import forms
from .models import TournamentRegistration

class TournamentRegistrationForm(forms.ModelForm):
    class Meta:
        model = TournamentRegistration
        fields = [
            'name',
            'surnames',
            'mail',
            'population',
            'zip_code',
            'date_birth',
            'phone',
            'privacy_policy',
            'tournament_title',
            'status'
        ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'surnames': forms.TextInput(attrs={'class': 'form-control'}),
            'population': forms.TextInput(attrs={'class': 'form-control'}),
            'zip_code': forms.TextInput(attrs={'class': 'form-control'}),
            'mail': forms.EmailInput(attrs={'class': 'form-control'}),
            'privacy_policy': forms.CheckboxInput(attrs={'class': 'form-check-label', 'required': True}),
            'phone': forms.TextInput(
                attrs={
                    "type": "tel",
                    "required": True,
                    "pattern": "[0-9]{3}-[0-9]{2}-[0-9]{2}-[0-9]{2}",
                    "placeholder": "123-45-67-89",
                    'class': 'form-control',
                }
            ),
            'date_birth': forms.TextInput(
                attrs={
                    'type': 'date',
                    'required': True,
                    'class': 'form-control',
                }
            )
        }