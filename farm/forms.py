from django import forms
from .models import Requisito


class RequisitoForm(forms.ModelForm):
    nota_complementaria = forms.CharField(required=False, widget=forms.Textarea)

    class Meta:
        model = Requisito
        fields = ['temperatura', 'humedad', 'ph_suelo', 'cantidad_riego', 'nota_complementaria']
