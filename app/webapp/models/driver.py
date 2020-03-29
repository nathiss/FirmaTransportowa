from django.db import models

from .person import Person
from .vehicle import Vehicle


class Driver(Person):
    class Meta:
        verbose_name = 'Driver'
        verbose_name_plural = 'Drivers'
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
