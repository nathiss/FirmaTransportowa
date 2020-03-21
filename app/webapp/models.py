import uuid

from django.db import models

class Person(models.Model):
    class Meta:
        abstract = True
        plural_name = 'People'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)


class Driver(Person):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)


class Client(Person):
    email = models.EmailField()


class Vehicle(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    registration_number = models.CharField(max_length=20)
    number_of_seats = models.IntegerField(validators=[MinValueValidator(1)])


class Place(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    city = models.CharField(max_length=50)
    street = models.CharField(max_length=50)
    stop_name = models.CharField(max_length=50)


class Connection(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    starting_place = models.ForeignKey(Place, on_delete=models.CASCADE)
    laststop_place = models.ForeignKey(Place, on_delete=models.CASCADE)
    price = models.IntegerField(validators=[MinValueValidator(0)])
    date_time = models.DateTimeField()


class Ticket(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    owner = models.ForeignKey(Client, on_delete=models.CASCADE)
    connection = models.ForeignKey(Connection, on_delete=models.CASCADE)


    
