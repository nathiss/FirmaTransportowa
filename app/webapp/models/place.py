import uuid

from django.db import models


class Place(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    city = models.CharField(max_length=50)
    street = models.CharField(max_length=50)
    stop_name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return f'{self.stop_name}'
