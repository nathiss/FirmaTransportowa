from django.shortcuts import render

from .index import IndexView
from .login import LoginView
from .logout import LogoutView
from .register  import RegisterView
from .change_password import ChangePasswordView
from .post import CreatePostView
from .post import DeletePostView
from .post import EditPostView
from .create_place import CreatePlaceView
from .create_connection import CreateConnectionView
from .ticket import CreateTicketView
from .my_tickets import TicketsView


def about_us(request, *args, **kwargs):
    return render(request, 'webapp/about_us.html')

def contact(request, *args, **kwargs):
    return render(request, 'webapp/contact.html')
