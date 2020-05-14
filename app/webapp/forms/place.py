from django import forms

from ..models import Place

class PlaceForm(forms.ModelForm):
    class Meta:
        model = Place
        fields = ['city', 'street', 'stop_name']
        labels = {
            'city': 'Miasto',
            'street': 'Ulica',
            'stop_name': 'Nazwa przystanku',
        }
