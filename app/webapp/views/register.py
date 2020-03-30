from django.views           import View
from django.shortcuts       import render, redirect
from django.contrib.auth    import authenticate

from ..forms import RegisterForm

class RegisterView(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('webapp:index')
        form = RegisterForm()
        return render(request, 'webapp/register.html', {"form": form})

    def post(self, request, *args, **kwargs):

        return render(request, 'webapp/register.html')
