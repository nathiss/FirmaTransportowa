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


def about_us(request, *args, **kwargs):
    return render(request, 'webapp/about_us.html')

def contact(request, *args, **kwargs):
    return render(request, 'webapp/contact.html')
