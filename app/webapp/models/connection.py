import uuid

from django.db import models
from django.core.validators import MinValueValidator

from .place import Place

class Connection(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    starting_place = models.ForeignKey(Place, related_name='FirstStop', on_delete=models.CASCADE)
    laststop_place = models.ForeignKey(Place, related_name='LastStop', on_delete=models.CASCADE)
    distance = models.PositiveIntegerField(help_text='Please enter the distance in kilometers.')
    price = models.PositiveIntegerField(validators=[MinValueValidator(1)], help_text='Please enter an integer value.')
    date_time = models.DateTimeField()

    def __str__(self):
        return f'[{self.date_time}] {self.starting_place} - {self.laststop_place}'
