from django import forms
from .models import Requisito, Cultivo


class CultivoForm(forms.ModelForm):
    DEPARTAMENTOS_COLOMBIA = [
        ('Amazonas', 'Amazonas'),
        ('Antioquia', 'Antioquia'),
        ('Arauca', 'Arauca'),
        ('Atlántico', 'Atlántico'),
        ('Bolívar', 'Bolívar'),
        ('Boyacá', 'Boyacá'),
        ('Caldas', 'Caldas'),
        ('Caquetá', 'Caquetá'),
        ('Casanare', 'Casanare'),
        ('Cauca', 'Cauca'),
        ('Cesar', 'Cesar'),
        ('Chocó', 'Chocó'),
        ('Córdoba', 'Córdoba'),
        ('Cundinamarca', 'Cundinamarca'),
        ('Guainía', 'Guainía'),
        ('Guaviare', 'Guaviare'),
        ('Huila', 'Huila'),
        ('La Guajira', 'La Guajira'),
        ('Magdalena', 'Magdalena'),
        ('Meta', 'Meta'),
        ('Nariño', 'Nariño'),
        ('Norte de Santander', 'Norte de Santander'),
        ('Putumayo', 'Putumayo'),
        ('Quindío', 'Quindío'),
        ('Risaralda', 'Risaralda'),
        ('San Andrés y Providencia', 'San Andrés y Providencia'),
        ('Santander', 'Santander'),
        ('Sucre', 'Sucre'),
        ('Tolima', 'Tolima'),
        ('Valle del Cauca', 'Valle del Cauca'),
        ('Vaupés', 'Vaupés'),
        ('Vichada', 'Vichada'),
    ]

    departamento = forms.ChoiceField(choices=DEPARTAMENTOS_COLOMBIA, label='Departamento')
    municipio = forms.CharField(max_length=100, label='Municipio')

    class Meta:
        model = Cultivo
        fields = ['nombre_cultivo', 'tipo_alimento', 'tipo_propagacion', 'departamento', 'municipio']


class RequisitoForm(forms.ModelForm):
    nota_complementaria = forms.CharField(required=False, widget=forms.Textarea)

    class Meta:
        model = Requisito
        fields = ['temperatura', 'humedad', 'ph_suelo', 'cantidad_riego', 'nota_complementaria']
