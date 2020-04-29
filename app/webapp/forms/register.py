from django                 import forms
from django.core.validators import RegexValidator

class RegisterForm(forms.Form):
    login = forms.CharField(label='Login użytkownika', max_length=100)
    passwd = forms.CharField(label='Hasło użytkownika', max_length=100, widget=forms.PasswordInput)
    repeatPasswd = forms.CharField(label='Powtórz hasło', max_length=100, widget=forms.PasswordInput)
    email = forms.EmailField(label='Email', max_length=100)

    first_name = forms.CharField(label='Imię', max_length=100)
    last_name = forms.CharField(label="Nazwisko", max_length=100)
    phone_number = forms.CharField(label='Numer telefonu', max_length=9, validators=[RegexValidator(regex=r'^[0-9]{9}$', message='Podany numer telefonu jest nieprawidłowy')])
    pesel = forms.CharField(label='PESEL', max_length=11, validators=[RegexValidator(regex=r'^[0-9]{11}$', message='Podany pesel jest nieprawidłowy')])


    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("passwd")
        repeat_password = cleaned_data.get("repeatPasswd")

        if password != repeat_password:
            raise forms.ValidationError("Podane hasła różnią się")

        return cleaned_data
