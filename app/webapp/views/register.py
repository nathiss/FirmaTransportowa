from django.views               import View
from django.shortcuts           import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth        import authenticate

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

            User.objects.create_user(username, None, password)
            authenticate(username=username, password=password)

            return redirect('webapp:index')
            
        return render(request, 'webapp/register.html', {"form": form})

