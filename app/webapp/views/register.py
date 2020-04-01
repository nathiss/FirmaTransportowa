from django.views               import View
from django.shortcuts           import render, redirect
from django.contrib.auth.models import User
from django.core.exceptions     import ObjectDoesNotExist

from ..forms import RegisterForm

class RegisterView(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('webapp:index')
        form = RegisterForm()
        return render(request, 'webapp/register.html', {"form": form})

    def post(self, request, *args, **kwargs):
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['login']
            password = form.cleaned_data['passwd']
            repeatPassword = form.cleaned_data['repeatPasswd']

            if (password != repeatPassword):
                form.add_error(field=None, error='Hasła nie zgadzają się.')
                return render(request, 'webapp/register.html', {"form": form})

            user = self.search(username)
            if user is True:
                form.add_error(field=None, error='Użytkownik już istnieje.')
                return render(request, 'webapp/register.html', {"form": form})

            user = User.objects.create_user(username, None, password)

            return render(request, 'webapp/register.html', {"form": form})

        form.add_error(field=None, error='Formularz jest nieprawidłowy.')
        return render(request, 'webapp/register.html', {"form": form})

    def search(self, userstring):
        try:
            User.objects.get(username=userstring)
            return True
        except ObjectDoesNotExist:
            return False
