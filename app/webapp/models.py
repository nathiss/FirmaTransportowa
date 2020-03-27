import uuid

from django.db import models
from django.core.validators import MinValueValidator, RegexValidator
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save


class Vehicle(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    registration_number = models.CharField(max_length=20, help_text='Max length: 20')
    number_of_seats = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    model_fullname = models.CharField(max_length=100, blank=True, default='Unknown', help_text='Please enter the full name of the vehicle model.')


class Person(models.Model):
    class Meta:
        abstract = True
        verbose_name = 'Person'
        verbose_name_plural = 'People'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=50, help_text='Max length: 50')
    last_name = models.CharField(max_length=50, help_text='Max length: 50')
    email = models.EmailField()
    phone_number = models.CharField(max_length=(9), validators=[
        RegexValidator(r'^[0-9]$', 'This is not a valid phone number.')
    ])
    pesel = models.CharField(max_length=(11), validators=[
        RegexValidator(r'^[0-9]$', 'This is not a valid PESEL number.')
    ])


class Driver(Person):
    class Meta:
        verbose_name = 'Driver'
        verbose_name_plural = 'Drivers'
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)


# https://simpleisbetterthancomplex.com/tutorial/2016/07/22/how-to-extend-django-user-model.html#onetoone
class Client(Person):
    class Meta:
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'
    user = models.OneToOneField(User, on_delete=models.CASCADE)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, *args, **kwargs):
    if created:
        # pylint: disable=no-member
        Client.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, *args, **kwargs):
    instance.client.save()


class Place(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    city = models.CharField(max_length=50)
    street = models.CharField(max_length=50)
    stop_name = models.CharField(max_length=50)


class Connection(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    starting_place = models.ForeignKey(Place, related_name='FirstStop', on_delete=models.CASCADE)
    laststop_place = models.ForeignKey(Place, related_name='LastStop', on_delete=models.CASCADE)
    distance = models.PositiveIntegerField(help_text='Please enter the distance in kilometers.')
    price = models.PositiveIntegerField(validators=[MinValueValidator(1)], help_text='Please enter an integer value.')
    date_time = models.DateTimeField()


class Ticket(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    owner = models.ForeignKey(Client, on_delete=models.CASCADE)
    connection = models.ForeignKey(Connection, on_delete=models.CASCADE)
