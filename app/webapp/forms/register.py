from django import forms
from django.contrib.auth.models import User
from django.core.exceptions     import ObjectDoesNotExist

class RegisterForm(forms.Form):
    login = forms.CharField(label='Login użytkownika', max_length=100)
    passwd = forms.CharField(label='Hasło użytkownika', max_length=100, widget=forms.PasswordInput)
    repeatPasswd = forms.CharField(label='Powtórz hasło', max_length=100, widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("login")
        password = cleaned_data.get("passwd")
        repeat_password = cleaned_data.get("repeatPasswd")

        if password != repeat_password:
            raise forms.ValidationError("Podane hasła różnią się")

        if len(password) < 8:
            raise forms.ValidationError("Hasło musi mieć co najmniej 8 znaków")

        user = self.search(username)
        if user is True:
            raise forms.ValidationError("Użytkownik o podanym loginie już istnieje")

    def search(self, userstring):
        try:
            User.objects.get(username=userstring)
            return True
        except ObjectDoesNotExist:
            return False
