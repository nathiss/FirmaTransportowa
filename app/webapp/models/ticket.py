import uuid

from django.db import models

from .connection import Connection
from .client import Client


class Ticket(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    owner = models.ForeignKey(Client, on_delete=models.CASCADE)
    connection = models.ForeignKey(Connection, on_delete=models.CASCADE)

    def __str__(self):
        return f'ticket-{self.id} ({self.connection})'
