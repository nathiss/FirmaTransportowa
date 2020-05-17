import uuid

from django.db import models
from django.core.validators import MinValueValidator


class Vehicle(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    registration_number = models.CharField(max_length=20, help_text='Max length: 20')
    number_of_seats = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    model_fullname = models.CharField(max_length=100, blank=True,
                                      default='Unknown',
                                      help_text='Please enter the full name of the vehicle model.')

    def __str__(self):
        return f'{self.registration_number}'
