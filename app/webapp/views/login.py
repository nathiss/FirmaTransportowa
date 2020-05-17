from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

from ..forms import LoginForm

class LoginView(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('webapp:index')
        form = LoginForm()
        return render(request, 'webapp/login.html', {"form": form})

    def post(self, request, *args, **kwargs):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['login']
            password = form.cleaned_data['passwd']
            remember_me = form.cleaned_data['remember_me']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                if not remember_me:
                    request.session.set_expiry(3600)
                return redirect('webapp:index')

            form.add_error(field=None, error='Nieprawidłowy login i/lub hasło.')
            return render(request, 'webapp/login.html', {"form": form})

        form.add_error(field=None, error='Formularz jest nieprawidłowy.')
        return render(request, 'webapp/login.html', {"form": form})
