from django import forms

class RegisterForm(forms.Form):
    login           = forms.CharField(label='Login użytkownika', max_length=100)
    passwd          = forms.CharField(label='Hasło użytkownika', max_length=100, widget=forms.PasswordInput)
    repeatPasswd    = forms.CharField(label='Powtórz hasło', max_length=100, widget=forms.PasswordInput)

