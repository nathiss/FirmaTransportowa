from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth import logout

from ..forms import ChangePasswordForm

class ChangePasswordView(View):
    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('webapp:index')

        form = ChangePasswordForm(request.user)
        return render(request, 'webapp/change_password.html', {'form': form})

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('webapp:index')

        form = ChangePasswordForm(user=request.user, data=request.POST)
        if form.is_valid():
            new_passwd = form.cleaned_data['new_password']
            request.user.set_password(new_passwd)
            request.user.save()

            logout(request)
            return redirect('webapp:login')

        return render(request, 'webapp/change_password.html', {'form': form})
