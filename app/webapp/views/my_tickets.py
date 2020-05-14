from django.views import View
from django.shortcuts import render, get_object_or_404, redirect

from ..models import Ticket, Client

class TicketsView(View):
    def get(self, request):
        if not request.user.is_authenticated:
            return redirect('webapp:index')

        me = get_object_or_404(Client, user=request.user)
        tickets = Ticket.objects.filter(owner=me)
        tickets = map(lambda ticket: ticket.connection, tickets)

        return render(request, 'webapp/my_tickets.html', {'tickets': tickets})
