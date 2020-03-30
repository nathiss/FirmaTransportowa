from django.contrib import admin

from .models import Client, Connection, Driver, Place, Post, Ticket, Vehicle

admin.site.register(Client)
admin.site.register(Connection)
admin.site.register(Driver)
admin.site.register(Place)
admin.site.register(Post)
admin.site.register(Ticket)
admin.site.register(Vehicle)
