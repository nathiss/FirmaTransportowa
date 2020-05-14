from django.views import View
from django.shortcuts import render, redirect
from django.http import Http404

from ..forms import ConnectionForm
from ..models import Place, Connection

class CreateConnectionView(View):
    def get(self, request):
        if not request.user.is_staff:
            raise Http404('Not found')

        form = ConnectionForm()
        starting_places = Place.objects.all()
        laststop_places = Place.objects.all()

        return render(request, 'webapp/create_connection.html', {
            'form': form,
            'starting_places': starting_places,
            'laststop_places': laststop_places,
        })

    def post(self, request):
        if not request.user.is_staff:
            raise Http404('Not found')

        form = ConnectionForm(request.POST)
        if not form.is_valid():
            starting_places = Place.objects.all()
            laststop_places = Place.objects.all()
            return render(request, 'webapp/create_connection.html', {
                'form': form,
                'starting_places': starting_places,
                'laststop_places': laststop_places,
            })

        connection = Connection()
        connection.distance = form.cleaned_data['distance']
        connection.price = form.cleaned_data['price']
        connection.date_time = form.cleaned_data['date_time']
        connection.starting_place = form.cleaned_data['starting_place']
        connection.laststop_place = form.cleaned_data['laststop_place']
        connection.save()

        return redirect('webapp:create_connection')
