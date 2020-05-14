from django.views import View
from django.shortcuts import render, redirect
from django.http import Http404

from ..forms import PlaceForm
from ..models import Place


class CreatePlaceView(View):
    def get(self, request):
        if not request.user.is_staff:
            raise Http404('Not found')

        form = PlaceForm()
        return render(request, 'webapp/create_place.html', {'form': form})

    def post(self, request):
        if not request.user.is_staff:
            raise Http404('Not found')

        form = PlaceForm(request.POST)
        if form.is_valid():
            p = Place()
            p.city = form.cleaned_data['city']
            p.street = form.cleaned_data['street']
            p.stop_name = form.cleaned_data['stop_name']
            p.save()
            return redirect('webapp:index')

        return render(request, 'webapp/create_place.html', {'form': form})
