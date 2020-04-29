import uuid

from django.db import models
from django.core.validators import RegexValidator

from .vehicle import Vehicle


class Driver(models.Model):
    class Meta:
        verbose_name = 'Driver'
        verbose_name_plural = 'Drivers'
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=50, help_text='Max length: 50')
    last_name = models.CharField(max_length=50, help_text='Max length: 50')
    email = models.EmailField()
    phone_number = models.CharField(max_length=(9), validators=[
        RegexValidator(r'^[0-9]{9}$', 'This is not a valid phone number.')
    ])
    pesel = models.CharField(max_length=(11), validators=[
        RegexValidator(r'^[0-9]{11}$', 'This is not a valid PESEL number.')
    ])

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
