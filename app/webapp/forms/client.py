from django import forms
from django.core.validators import RegexValidator

class ClientForm(forms.Form):
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Podany numer telefonu jest nieprawidłowy")
    pesel_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Podany pesel jest nieprawidłowy")

    first_name = forms.CharField(label='Imię', max_length=100)
    last_name = forms.CharField(label='Nazwisko', max_length=100)
    phone_number = forms.CharField(label='Numer telefonu', validators=[phone_regex], max_length=17)
    pesel = forms.CharField(label='Pesel', validators=[pesel_regex], max_length=10, min_length=10)
