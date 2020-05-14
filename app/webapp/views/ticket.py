from django.views import View
from django.shortcuts import render, redirect, get_object_or_404

from ..forms import TicketForm
from ..models import Connection, Ticket, Client

class CreateTicketView(View):
    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('webapp:index')

        form = TicketForm()
        connections = Connection.objects.all()
        return render(request, 'webapp/create_ticket.html', {'form': form, 'connections': connections})

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('webapp:index')

        form = TicketForm(request.POST)
        if not form.is_valid():
            connections = Connection.objects.all()
            return render(request, 'webapp/create_ticket.html', {'form': form, 'connections': connections})

        ticket = Ticket()
        ticket.owner = get_object_or_404(Client, user=request.user)
        ticket.connection = form.cleaned_data['connection']
        ticket.save()

        return redirect('webapp:create_ticket')

