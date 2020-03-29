from django import forms


class LoginForm(forms.Form):
    login = forms.CharField(label='Login użytkownika', max_length=100)
    passwd = forms.CharField(label='Hasło użytkownika', max_length=100, widget=forms.PasswordInput)
    remember_me = forms.BooleanField(label='Zapamiętaj mnie', required=False)
