from django import forms
from .models import DutyOfficer

class DutyOfficerForm(forms.ModelForm):
    class Meta:
        model = DutyOfficer
        fields = ['position', 'rank', 'full_name', 'weapon_number',]
        widgets = {
            'position': forms.TextInput(attrs={'class': 'form-control'}),
            'rank': forms.TextInput(attrs={'class': 'form-control'}),
            'full_name': forms.TextInput(attrs={'class': 'form-control'}),
            'weapon_number': forms.TextInput(attrs={'class': 'form-control'}),
        }