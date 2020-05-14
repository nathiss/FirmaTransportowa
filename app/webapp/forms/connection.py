import datetime

from django import forms

from ..models import Place, Connection

class ConnectionForm(forms.Form):
    distance = forms.IntegerField(min_value=1, label='Odległość pomiędzy przystankami w kilometrach')
    price = forms.IntegerField(min_value=1, label='Cena za bilet w złotówkach')
    date_time = forms.DateTimeField(label='Data odjazdu', required=False)
    starting_place = forms.UUIDField(label='Nazwa przystanku startowego')
    laststop_place = forms.UUIDField(label='Nazwa ostatniego przystanku')

    def clean(self):
        cleaned_data = super().clean()
        starting = cleaned_data['starting_place']
        laststop = cleaned_data['laststop_place']

        if starting == laststop:
            raise forms.ValidationError('Przystanek początkowy i ostatni muszą być różne')

        try:
            cleaned_data['starting_place'] = Place.objects.get(pk=starting)
            cleaned_data['laststop_place'] = Place.objects.get(pk=laststop)
        except:
            raise forms.ValidationError('Przystanek początkowy i/lub końcowy nie istnieje')

        same_connections = Connection.objects.filter(starting_place=cleaned_data['starting_place'], laststop_place=cleaned_data['laststop_place']).count()
        if same_connections != 0:
            raise forms.ValidationError(f'Takie połączenie już istnieje ({cleaned_data["starting_place"]} -> {cleaned_data["laststop_place"]})')

        if cleaned_data['date_time'] is None or cleaned_data['date_time'] == '':
            cleaned_data['date_time'] = datetime.datetime.now()

        return cleaned_data
