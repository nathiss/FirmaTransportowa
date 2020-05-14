from django import forms

from ..models import Connection

class TicketForm(forms.Form):
    connection = forms.UUIDField(label='Połączenie')

    def clean(self):
        cleaned_data = super().clean()
        connection_id = cleaned_data['connection']

        try:
            cleaned_data['connection'] = Connection.objects.get(id=connection_id)
        except:
            raise forms.ValidationError('Takie połączenie nie istnieje')

        return cleaned_data

