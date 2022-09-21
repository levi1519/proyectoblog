from dataclasses import fields
from django import forms
from .models import Ropa

class RopaForm(forms.ModelForm):
    class Meta:
        model = Ropa
        fields ='__all__'