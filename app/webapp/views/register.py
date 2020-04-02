from django.views               import View
from django.shortcuts           import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth        import login

from ..forms    import RegisterForm
from ..forms    import ClientForm
from ..models   import Client

class RegisterView(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('webapp:index')
        form = RegisterForm()
        client_form = ClientForm()
        return render(request, 'webapp/register.html', {"form": form, "client_form": client_form})

    def post(self, request, *args, **kwargs):
        form = RegisterForm(request.POST)
        client_form = ClientForm()
        if form.is_valid() and client_form.is_valid():
            username = form.cleaned_data['login']
            password = form.cleaned_data['passwd']
            email = form.cleaned_data['email']

            first_name = client_form.cleaned_data['first_name']
            last_name = client_form.cleaned_data['last_name']
            phone_number = client_form.cleaned_data['phone_number']
            pesel = client_form.cleaned_data['pesel']

            user = User.objects.create_user(username, email, password)
            Client.create(first_name=first_name, last_name=last_name, email=email, phone_number=phone_number, pesel=pesel, user=user)

            login(user, request)

            return redirect('webapp:index')

        return render(request, 'webapp/register.html', {"form": form, "client_form": client_form})
