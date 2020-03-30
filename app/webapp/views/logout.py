from django.views import View
from django.shortcuts import redirect
from django.contrib.auth import logout


class LogoutView(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            logout(request)
        return redirect('webapp:index')
