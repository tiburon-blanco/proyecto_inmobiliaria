import django_filters
from django import forms

from app.propiedad.models import TipoPropiedad, Propiedad


class PropiedadForm(forms.ModelForm):
    calle = forms.TextInput()
    numero = forms.TextInput()
    tipoPropiedad = django_filters.ModelChoiceFilter(queryset=TipoPropiedad.objects.all())

    class Meta:
        model = Propiedad
        fields = ['calle', 'numero', 'tipoPropiedad']
