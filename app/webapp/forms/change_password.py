from django import forms

class ChangePasswordForm(forms.Form):
    old_password = forms.CharField(label='Stare Hasło', max_length=100, widget=forms.PasswordInput)
    new_password = forms.CharField(label='Nowe hasło', max_length=100, widget=forms.PasswordInput)
    new_password_repeat = forms.CharField(
        label='Powtórz nowe hasło', max_length=100, widget=forms.PasswordInput)

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if user is None:
            raise Exception('pls, nie utrudniaj')
        self.user = user


    def clean(self):
        cleaned_data = super().clean()
        cleaned = {
            'old_password': cleaned_data.get('old_password'),
            'new_password': cleaned_data.get('new_password'),
            'new_password_repeat': cleaned_data.get('new_password_repeat')
        }

        if not self.user.check_password(cleaned['old_password']):
            raise forms.ValidationError('Podane stare hasło jest błędne')

        if cleaned['new_password'] != cleaned['new_password_repeat']:
            raise forms.ValidationError('Hasła się różnią')

        if self.user.check_password(cleaned['new_password']):
            raise forms.ValidationError('Nowe hasło jest takie samo jak stare')

        return cleaned_data
