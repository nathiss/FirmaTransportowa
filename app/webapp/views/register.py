from django.views               import View
from django.shortcuts           import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth        import login

from ..forms    import RegisterForm
from ..models   import Client

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
            email = form.cleaned_data['email']

            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            phone_number = form.cleaned_data['phone_number']
            pesel = form.cleaned_data['pesel']

            user = User.objects.create_user(username, email, password)
            client = Client(first_name=first_name, last_name=last_name, email=email, phone_number=phone_number, pesel=pesel, user=user)
            client.save()

            login(request, user)

            return redirect('webapp:index')

        return render(request, 'webapp/register.html', {"form": form})
